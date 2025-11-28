from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def receive_webhook():
    if request.is_json:
        data = request.get_json()
        print("Received JSON data:", data)
            # Process the data here (e.g., save to database, trigger another action)
        return jsonify({"status": "success", "message": "Webhook received"}), 200
    else:
        print("Received non-JSON data:", request.data)
        return jsonify({"status": "error", "message": "Expected JSON payload"}), 400

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
