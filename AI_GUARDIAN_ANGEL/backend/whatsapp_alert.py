from predictor import predict_risk
from twilio.rest import Client

ACCOUNT_SID = "ACxxxx"
AUTH_TOKEN = "your_token"

def send_whatsapp_alert():
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='🚨 Fall or High Risk Detected!',
        to='whatsapp:+91XXXXXXXXXX'
    )

def run_ai(steps, sleep, water):
    risk = predict_risk(steps, sleep, water)

    print("Risk:", risk)

    if risk == "High":
        send_whatsapp_alert()
        return "High Risk - Alert Sent!"
    else:
        return "Low Risk - Safe"