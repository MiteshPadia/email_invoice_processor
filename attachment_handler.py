# attachment_handler.py

import os
from config import ATTACHMENT_DIR
from db import save_attachment_metadata

# Create attachment directory if it does not exist
if not os.path.exists(ATTACHMENT_DIR):
    os.makedirs(ATTACHMENT_DIR)


def process_attachments(email_message):
    message_id = email_message.get("Message-ID")

    for part in email_message.walk():
        # Skip non-attachment parts
        if part.get_content_disposition() != "attachment":
            continue

        filename = part.get_filename()

        # Process only PDF files
        if not filename or not filename.lower().endswith(".pdf"):
            continue

        payload = part.get_payload(decode=True)
        if not payload:
            continue

        file_path = os.path.join(ATTACHMENT_DIR, filename)

        # Avoid overwriting files with the same name
        if os.path.exists(file_path):
            continue

        with open(file_path, "wb") as file:
            file.write(payload)

        metadata = {
            "message_id": message_id,
            "filename": filename,
            "file_path": os.path.abspath(file_path)
        }

        save_attachment_metadata(metadata)
