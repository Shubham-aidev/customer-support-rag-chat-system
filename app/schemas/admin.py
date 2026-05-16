from pydantic import BaseModel#, EmailStr, Field , field_validator

# document upload request schema
class DocumentRequest(BaseModel):

    title:str
    department:str
    document_type:str
    version:int
    file_content:str

# document upload response schema
class DocumentResponse(BaseModel):

    id:int
    title:str
    document_type:str
    department:str
    version:int

    class Config:
        from_attributes=True





