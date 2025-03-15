from requests import get
from flask import Flask, request, render_template
from google import genai
from dotenv import load_dotenv
from os import getenv


app = Flask(__name__)

load_dotenv()


token = getenv("TELEGRAM_TOKEN")

def get_send_message(chat_id, text):
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    return get(f"https://api.telegram.org/bot{token}/sendMessage", json=payload)


@app.route('/')
def index():
    if request.method == 'POST':
        data = request.get_json()
        chat_id = data['message']['chat']['id']
        text = data['message']['text']

         

    return render_template("index.html")

if __name__ == "__main__":
    app.run()
