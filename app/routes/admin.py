from fastapi import APIRouter, Depends, Form, UploadFile, File
from sqlalchemy.orm import Session
from dependencies import get_db, require_admin
from schemas.document import DocumentResponse, DocumentMetaData
from services.admin import upload_docs
from models.user import User

router = APIRouter()


# file upload api
@router.post("/documents",response_model=DocumentResponse)
async def upload_api(title:str = Form(...),
               document_type:str = Form(...),
               department:str = Form(...),
               version:int = Form(...),
               file:UploadFile = File(...),
               
               admin:User = Depends(require_admin),
               db:Session = Depends(get_db)):
    
    meta_data = DocumentMetaData(
                                title=title,
                                document_type=document_type,
                                department=department,
                                version=version)
    

    return await upload_docs(meta_data, file, admin, db)