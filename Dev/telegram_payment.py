import requests

BOT_TOKEN = "8527010409:AAHQOxd8F26aCrqTCkn55-6jjMLHxqvEYew"
CHAT_ID = "1875145789"

def send_payment(name, amount, utr):

    message = f"""
✅ New Payment Request

Name: {name}
Amount: ₹{amount}
UTR: {utr}
"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(url, data=data)
