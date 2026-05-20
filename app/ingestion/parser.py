from ingestion.extractor import extract_text
from models.document import Document
from sqlalchemy.orm import Session

def parse_document(document_id:int, db:Session):

    document = db.query(Document).filter(
        Document.id == document_id
    ).first()

    if not document:
        raise ValueError("Document not found")

    filepath = document.storage_path

    json_output = extract_text(filepath,document)

    #return json_output
    print(json_output)