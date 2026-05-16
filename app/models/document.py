# models/user.py
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from database.db import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Document(Base):

    __tablename__ = "documents"

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String,unique=True,index=True,nullable=False)
    document_type = Column(String,index=True,nullable=False)
    storage_path = Column(String,unique=True,nullable=False)
    ingestion_status = Column(String,index=True,nullable=False)
    uploaded_by_admin_id = Column(Integer,index=True,nullable=False)
    created_at = Column(DateTime,index=True,default=func.now(),nullable=False)
    updated_at = Column(DateTime,index=True,default=func.now(),onupdate=func.now())

    def __repr__(self):
        return f"<Admin id={self.uploaded_by_admin_id} document_title={self.title}>"


#     documents
# (
#   id UUID PK,
#   title VARCHAR NOT NULL,
#   document_type VARCHAR,
#   storage_path TEXT NOT NULL,
#   ingestion_status VARCHAR NOT NULL,
#   uploaded_by_admin_id UUID,
#   created_at TIMESTAMP,
#   updated_at TIMESTAMP
# )

