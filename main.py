import requests
import time
import csv
import datetime
import sys

# Set expiration date
EXPIRE_ON = datetime.datetime(2025, 8, 23) # vienti dia pero ahora

# ===== EXPIRATION CHECK =====
EXPIRE_ON = datetime.datetime(2025, 8, 23)  # vienti dia pero ahora
if datetime.datetime.now() > EXPIRE_ON:
    print("⛔ This script has expired. Please contact the developer.")
    sys.exit(1)


RESEND_API_KEY = 're_dEQyGG4b_3rTKvQXpY6vYqRXF2RkgAaYB'
FROM_EMAIL = 'CryptInfo Inc. <noreply@cryptinfo.info>'  # Use your verified sender email here
LOG_FILE = 'email_send_log.csv'
EMAILS_FILE = 'recipients.txt'  # Your .txt file with emails, one per line
TEMPLATE_FILE = 'email_template.html'

def send_email(to_email, subject, html_body, retries=3):
    url = "https://api.resend.com/emails"
    headers = {
        "Authorization": f"Bearer {RESEND_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "from": FROM_EMAIL,
        "to": [to_email],
        "subject": subject,
        "html": html_body,
        "text": "Please view this email in an HTML-compatible client."
    }

    for attempt in range(1, retries + 1):
        try:
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code in (200, 202):
                return {"success": True, "email": to_email, "msg": "Sent"}
            else:
                return {"success": False, "email": to_email, "msg": response.text}
        except Exception as e:
            if attempt == retries:
                return {"success": False, "email": to_email, "msg": str(e)}
            time.sleep(2)

def log_result(email, success, msg):
    with open(LOG_FILE, mode='a', newline='', encoding='utf-8') as log_file:
        writer = csv.writer(log_file)
        writer.writerow([email, success, msg])

def extract_name(email):
    """
    Extract a simple name from the email address, e.g. 'john.doe@example.com' -> 'John Doe'
    """
    local_part = email.split('@')[0]
    parts = local_part.replace('.', ' ').replace('_', ' ').split()
    name = ' '.join(part.capitalize() for part in parts if part)
    return name or "there"  # fallback

def load_emails_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        # Read lines, strip whitespace, ignore empty lines
        emails = [line.strip() for line in f if line.strip()]
    return emails

def main():
    # Load HTML template
    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        html_template = f.read()

    # Load emails from .txt file
    emails = load_emails_from_txt(EMAILS_FILE)
    print(f"Loaded {len(emails)} emails from {EMAILS_FILE}")

    subject = "🎉 Welcome to YourApp – We’re glad you're here!"

    for email in emails:
        name = extract_name(email)
        personalized_html = html_template.replace("{{ name }}", name)

        result = send_email(email, subject, personalized_html)
        log_result(email, result["success"], result["msg"])

        if result["success"]:
            print(f"[✅] Sent to {name} ({email})")
        else:
            print(f"[❌] Failed to send to {email}: {result['msg']}")

if __name__ == "__main__":
    main()
