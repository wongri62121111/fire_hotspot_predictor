import smtplib
from email.mime.text import MIMEText
from twilio.rest import Client

# Email configuration
EMAIL_SENDER = "your_email@example.com"
EMAIL_PASSWORD = "your_password"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
EMAIL_RECIPIENT = "recipient_email@example.com"

# Twilio configuration
TWILIO_ACCOUNT_SID = "your_twilio_account_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_PHONE_NUMBER = "+1234567890"  # Your Twilio phone number
RECIPIENT_PHONE_NUMBER = "+0987654321"  # Target phone number

def send_email_alert(anomaly_details):
    """
    Sends an email alert for detected anomalies.
    Args:
        anomaly_details (str): Description of the anomaly.
    """
    subject = "Wildfire Sensor Alert"
    body = f"Anomaly detected:\n{anomaly_details}"

    # Create the email message
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECIPIENT

    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECIPIENT, msg.as_string())
        print("Email alert sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

def send_sms_alert(anomaly_details):
    """
    Sends an SMS alert for detected anomalies.
    Args:
        anomaly_details (str): Description of the anomaly.
    """
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    try:
        message = client.messages.create(
            body=f"Wildfire Sensor Alert:\n{anomaly_details}",
            from_=TWILIO_PHONE_NUMBER,
            to=RECIPIENT_PHONE_NUMBER
        )
        print("SMS alert sent successfully!")
    except Exception as e:
        print(f"Failed to send SMS: {e}")
