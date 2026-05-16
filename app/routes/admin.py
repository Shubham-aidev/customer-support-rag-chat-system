from fastapi import APIRouter, Depends, Form, UploadFile, File
from sqlalchemy.orm import Session
from dependencies import get_db
from schemas.admin import DocumentResponse, DocumentRequest
from services.admin import upload_docs



router = APIRouter()

@router.post("/documents",response_model=DocumentResponse)
def upload_api(title:str = Form(...),
               document_type:str = Form(...),
               department:str = Form(...),
               version:str = Form(...),
               file:UploadFile = File(...),
               
               db:Session = Depends(get_db)):
    
    meta_data = {"title":title,
                 "document_type":document_type,
                 "department":department,
                 "version":version,
                 "file":file}

    return upload_docs(meta_data, db)