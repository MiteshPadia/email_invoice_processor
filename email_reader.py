# email_reader.py

import imaplib
from email import message_from_bytes
from email.header import decode_header
from config import IMAP_SERVER, EMAIL_USER, EMAIL_PASSWORD, KEYWORDS


class EmailReader:

    def connect(self):
        self.imap = imaplib.IMAP4_SSL(IMAP_SERVER)
        self.imap.login(EMAIL_USER, EMAIL_PASSWORD)
        self.imap.select("INBOX")

    def disconnect(self):
        self.imap.logout()

    def fetch_recent_emails(self, limit=20):
        status, data = self.imap.search(None, "ALL")
        email_ids = data[0].split()
        return email_ids[-limit:]

    def get_subject(self, msg):
        subject, _ = decode_header(msg["Subject"])[0]

        if isinstance(subject, bytes):
            subject = subject.decode("utf-8", errors="ignore")

        return subject

    def get_body(self, msg):
        body = ""

        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                payload = part.get_payload(decode=True)
                if payload:
                    body = payload.decode("utf-8", errors="ignore")
                break

        return body

    def email_matches_keywords(self, subject, body):
        text = f"{subject} {body}".lower()
        return any(keyword in text for keyword in KEYWORDS)

    def read_matching_emails(self):
        self.connect()
        matched_emails = []

        for email_id in self.fetch_recent_emails():
            status, msg_data = self.imap.fetch(email_id, "(RFC822)")
            msg = message_from_bytes(msg_data[0][1])

            subject = self.get_subject(msg)
            body = self.get_body(msg)

            if self.email_matches_keywords(subject, body):
                matched_emails.append(msg)

        self.disconnect()
        return matched_emails
