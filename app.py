from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>RIYA-PRO OB52 SERVER ACTIVE ✅</h1>"

@app.route('/api/v1/like', methods=['GET'])
def start_push():
    uid = request.args.get('uid', '11540742744')
    region = request.args.get('region', 'ind')
    
    # Real Garena Bridge Link
    target = f"https://freefire-api-five.vercel.app/api/v1/like?uid={uid}&region={region}"
    
    try:
        res = requests.get(target, timeout=15)
        return jsonify({
            "status": "success",
            "owner": "RIYA-PRO",
            "target_uid": uid,
            "server_msg": "Packet Injected to Garena Live",
            "season": "0", "level": "2"
        })
    except:
        return jsonify({"status": "error", "msg": "Server Busy"}), 500

if __name__ == "__main__":
    app.run()
