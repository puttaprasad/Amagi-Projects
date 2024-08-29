import os
import subprocess
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

def generate_report():
    # Define the folder path and report file
    folder_path = 'test_reports/Amagi_Tasks/reports'
    os.makedirs(folder_path, exist_ok=True)  # Create the folder if it doesn't exist
    report_path = os.path.join(folder_path, 'report.html')

    # Run pytest to generate the HTML report
    subprocess.run(['pytest', '--html=' + report_path, '--self-contained-html'])
    
    return report_path

def send_email(report_path, sender_email, sender_password, receiver_email):
    try:
        # Check if the report file exists
        if not os.path.exists(report_path):
            print(f"Report file not found: {report_path}")
            return

        # Create the email object
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = "Pytest HTML Report"

        # Attach the body text
        body = "Please find attached the pytest HTML report."
        msg.attach(MIMEText(body, 'plain'))

        # Attach the HTML report
        with open(report_path, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename={os.path.basename(report_path)}")
        msg.attach(part)

        # Sending the email
        print("Connecting to SMTP server...")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.set_debuglevel(1)  # Enable debug output to see the SMTP communication
        server.starttls()

        print("Logging in to SMTP server...")
        server.login(sender_email, sender_password)

        print("Sending email...")
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    # Generate the report
    report_path = generate_report()

    # Send the report via email
    send_email(report_path, sender_email, password, receiver_email)
