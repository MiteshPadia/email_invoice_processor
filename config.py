# email_invoice_processor/
# │
# ├── config.py              # All environment variables & constants
# ├── email_reader.py        # Gmail IMAP logic
# ├── attachment_handler.py  # Save + deduplicate attachments
# ├── textract_processor.py  # AWS Textract logic
# ├── db.py                  # MongoDB access
# ├── scheduler.py           # Periodic execution
# └── main.py                # Orchestration

# config.py
import os

IMAP_SERVER = "imap.gmail.com"
IMAP_PORT = 993

EMAIL_USER = os.getenv("mipa64566@gmail.com")
EMAIL_PASSWORD = os.getenv("notdecided")

KEYWORDS = ["invoice", "bill"]

ATTACHMENT_DIR = "./attachments"

MONGO_URI = "mongodb://localhost:27017/"
MONGO_DB = "pdf_paths"
MONGO_COLLECTION = "path"
