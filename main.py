from email_reader import EmailReader
from attachment_handler import process_attachments

def run_pipeline():
    try:
        print("Starting email processing pipeline")

        reader = EmailReader()
        emails = reader.read_matching_emails()

        for email in emails:
            process_attachments(email)

        print("Pipeline completed successfully")

    except Exception as e:
        print(f"Pipeline failed due to unexpected error: {e}")
