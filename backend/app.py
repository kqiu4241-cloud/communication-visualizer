from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import time

app = Flask(__name__)
CORS(app)

@app.route("/api/simulate", methods=["POST"])
def simulate_signal():
    data = request.json
    source = data.get("source", "A")
    destination = data.get("destination", "B")

    # 模拟通信参数
    delay_ms = round(random.uniform(20, 120), 2)
    bandwidth_mbps = round(random.uniform(10, 200), 2)
    snr_db = round(random.uniform(5, 40), 2)
    packet_loss = round(random.uniform(0, 5), 2)

    # 模拟延迟
    time.sleep(1)

    return jsonify({
        "source": source,
        "destination": destination,
        "delay_ms": delay_ms,
        "bandwidth_mbps": bandwidth_mbps,
        "snr_db": snr_db,
        "packet_loss": packet_loss
    })

if __name__ == "__main__":
    app.run(debug=True)
