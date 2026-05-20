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

    for para in doc.paragraphs:
        text = para.text.strip()
        if not text:
            continue  # Skip empty paragraphs
            
        # Check if the paragraph is a Heading (e.g., 'Heading 1', 'Heading 2')
        if para.style.name.startswith('Heading'):
            # If we already have an active section, save it before starting a new one
            if current_section:
                result["sections"].append(current_section)
                
            # Start a new section dictionary
            current_section = {
                "heading": text,
                "content": []
            }
        else:
            # It's regular body text or a list item
            if current_section:
                current_section["content"].append(text)
            else:
                # Fallback: Capture text that appears before any heading exists
                current_section = {
                    "heading": "Introduction",
                    "content": [text]
                }

    # Append the very last section processed
    if current_section:
        result["sections"].append(current_section)

    # Convert the Python dictionary to a formatted JSON string
    return result

# --- Usage Example ---
# json_output = docx_to_structured_json("refund_policy.docx")
# print(json_output)
