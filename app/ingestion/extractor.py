import os
import json
import docx
from models.document import Document
from uuid import uuid4

def extract_text(filepath:str,document:Document):
    doc = docx.Document(filepath)
    
    # Initialize the base JSON structure
    result = {
        "document_name": document.document_type + '_' + str(uuid4().hex[:4]),
        "sections": []
    }
    
    current_section = None
    print(doc.paragraphs)

    # for para in doc.paragraphs:
    #     text = para.text.strip()
    #     if not text:
    #         continue  # Skip empty paragraphs
            

# --- Usage Example ---
# json_output = docx_to_structured_json("refund_policy.docx")
# print(json_output)
