# service/admin.py
#from fastapi import HTTPException
import logging
#from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
#from models.user import User
from schemas.admin import DocumentRequest
import os
logger = logging.getLogger(__name__)


# document upload function
def upload_docs(meta_data:dict,db:Session):
    # make the directory
    os.makedirs("s3", exist_ok=True)

    # validate the file

    # save the file


    # create row in document table

    #return db_doc