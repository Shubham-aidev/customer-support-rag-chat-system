from pydantic import BaseModel#, EmailStr, Field , field_validator



class DocumentMetaData(BaseModel):
    title: str
    document_type: str
    department: str
    version: int


# document upload response schema
class DocumentResponse(BaseModel):

    id:int
    title:str
    document_type:str
    department:str
    version:int

    class Config:
        from_attributes=True





