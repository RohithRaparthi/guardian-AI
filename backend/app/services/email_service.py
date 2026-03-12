import smtplib
from email.mime.text import MIMEText
from app.services import monitoring_state


def send_fall_email():
    if not monitoring_state.selected_guardian_email:
        return

    sender = "rohithraprthi1437@gmail.com"
    password = "wsvi jepy dotl fpvm"  # 🔴 Replace with App Password
    receiver = monitoring_state.selected_guardian_email

    msg = MIMEText("⚠️ Fall detected! Immediate attention required.")
    msg["Subject"] = "Fall Detection Alert"
    msg["From"] = sender
    msg["To"] = receiver

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print("Email error:", e)