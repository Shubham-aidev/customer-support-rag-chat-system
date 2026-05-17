# service/admin.py
from fastapi import HTTPException, UploadFile
import logging
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from models.document import Document
from models.user import User
from schemas.document import DocumentMetaData
import os
from uuid import uuid4
logger = logging.getLogger(__name__)

# file validation function
async def file_validation(file:UploadFile):
    
    ALLOWED_EXTENSIONS = ['.pdf','.docx']
    MAX_FILE_SIZE = 5 * 1024 * 1024 # 5 Mb size
    ALLOWED_CONTENT_TYPES = {
                            "application/pdf",
                            "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                            }

    # check empty upload
    if not file.filename:
        raise HTTPException(status_code=400,
                            detail="filename is empty")
    
    # validate the file_extension
    ext = os.path.splitext(file.filename)[1].lower() 
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400,
                            detail="Only Pdf, docx file are allowed")
    
    # validate the file_size
    content = await file.read()
    if (len(content)) > MAX_FILE_SIZE:
        raise HTTPException(status_code=400,
                            detail="Max file size allowed is 5 mb")
    await file.seek(0) 
    
    # validate file content-type
    if file.content_type not in ALLOWED_CONTENT_TYPES:
        raise HTTPException(status_code=400,
                            detail="Invalid file content-type")
    
    # safe filename
    safe_filename = f"{uuid4()}{ext}"
    
    return safe_filename, content



    


# document upload function
async def upload_docs(meta_data:DocumentMetaData,file:UploadFile,admin:User,db:Session):
    
    os.makedirs("s3",exist_ok=True)
    # validate the file 

    safe_filename, content = await file_validation(file)
    
    # create filepath
    filepath = f"s3/{safe_filename}"
    
     # create row for document table
    db_row = Document(title=meta_data.title,
                      document_type=meta_data.document_type,
                      storage_path=filepath,
                      uploaded_by_admin_id=admin.id,
                      department=meta_data.department,
                      version=meta_data.version)
    
    try:
        with open(filepath,'wb') as buffer:
            buffer.write(content)
        
        db.add(db_row)
        db.commit()
        db.refresh(db_row)
        return db_row
    
    except IntegrityError as e:
        
        if os.path.exists(filepath):
            os.remove(filepath)
        
        db.rollback()

        raise HTTPException(status_code=400,
                            detail="database contraints violation")
    
    except Exception as e:
        
        if os.path.exists(filepath):
            os.remove(filepath)
        
        db.rollback()
        raise
    
    