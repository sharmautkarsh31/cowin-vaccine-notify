import boto3
from botocore.exceptions import ClientError

from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

SENDER = "apankhu@amazon.com"
RECIPIENT = ["pankhuriagarwal@outlook.com"]
AWS_REGION = "us-east-1"
SUBJECT = "CoWin Found Vaccine Sessions"
ses_client = boto3.client('ses', region_name=AWS_REGION)

def send_email(filename):
    message = MIMEMultipart('mixed')
    message['Subject'] = SUBJECT
    message['From'] = SENDER
    message['To'] = ",".join(RECIPIENT)

    msg_body = MIMEMultipart('alternative')
    _body = "Matched Session details attached"
    part = MIMEText(_body, 'html')
    msg_body.attach(part)

    part = MIMEApplication(open(filename, 'rb').read())
    name = 'Matched-sessions.csv'
    part.add_header('Content-Disposition', 'attachment', filename=name)
    msg_body.attach(part)

    message.attach(msg_body)

    response = ses_client.send_raw_email(Source=message['From'],
                                        Destinations=RECIPIENT,
                                        RawMessage={'Data': message.as_string()})
    print(response)