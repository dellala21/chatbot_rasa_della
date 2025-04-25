from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return "Chatbot Rasa sedang berjalan di Railway!"

@app.route('/webhook', methods=['POST'])
def webhook():
    return "Webhook diterima!"

if __name__ == '__main__':
    # Jalankan Rasa server di background
    subprocess.Popen(["rasa", "run", "--enable-api", "--cors", "*", "--connector", "telegram"])
    app.run(host='0.0.0.0', port=5000)
