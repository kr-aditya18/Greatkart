import requests
from django.conf import settings

def send_resend_email(subject, html, to_email):
    try:
        response = requests.post(
            "https://api.resend.com/emails",
            headers={
                "Authorization": f"Bearer {settings.RESEND_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "from": settings.DEFAULT_FROM_EMAIL,
                "to": [to_email],
                "subject": subject,
                "html": html,
            },
            timeout=5
        )
        return response.status_code in [200, 201]
    except Exception as e:
        print("RESEND EMAIL ERROR:", e)
        return False
