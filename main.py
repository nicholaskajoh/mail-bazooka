import sys
import requests

# USAGE EXAMPLE
# FORMAT: python main.py [MAILGUN-API-BASE-URL] [MAILGUN-API-KEY] [FROM-EMAIL] [T0-EMAIL-LIST] [EMAIL-SUBJECT] [EMAIL-BODY]
# SAMPLE: python main.py "https://api.mailgun.net/v3/samples.mailgun.org/messages" "key-3ax6xnjp29jd6fds4gc373sgvjxteol0" "Vandal Savage <vandalis@savage.io>" "email_list.example.txt" "I'm Savage" "email_body.example.txt"

def get_emails():
  with open(sys.argv[4], 'r') as data:
    emails = [email.rstrip() for email in data]
    return emails

def send():
  api_base_url = sys.argv[1]
  api_key = sys.argv[2]
  from_email = sys.argv[3]
  to_email_list = get_emails()
  subject = sys.argv[5]
  with open(sys.argv[6], 'r') as email_body:
    body = email_body.read()

  return requests.post(
    api_base_url,
    auth=("api", api_key),
    data={"from": from_email, "to": to_email_list, "subject": subject, "text": body})

send()
print("Done!")