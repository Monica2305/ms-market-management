# whats_app.py (HTTP)
import requests

TWILIO_API_URL = "https://api.twilio.com/send_message"

def send_whatsapp_message(phone, message):
    payload = {"phone": phone, "message": message}
    response = requests.post(TWILIO_API_URL, json=payload)
    return response.json()
