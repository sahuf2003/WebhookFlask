import os
from flask import Flask, request, jsonify

app = Flask(__name__)

import logging

app.logger.setLevel(logging.INFO)

@app.route('/webhook', methods=['POST'])
def receive_webhook():
    if request.is_json:
        data = request.get_json()
        app.logger.info(f"Received JSON data: {data}")
        return jsonify({"status": "success", "message": "Webhook received"}), 200
    else:
        app.logger.warning(f"Received non-JSON data: {request.data}")
        return jsonify({"status": "error", "message": "Expected JSON payload"}), 400

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
