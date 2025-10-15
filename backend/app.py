from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import random
import time
import os

app = Flask(__name__)
CORS(app)

@app.route("/api/simulate", methods=["POST"])
def simulate_signal():
    data = request.json
    source = data.get("source", "A")
    destination = data.get("destination", "B")

    delay_ms = round(random.uniform(20, 120), 2)
    bandwidth_mbps = round(random.uniform(10, 200), 2)
    snr_db = round(random.uniform(5, 40), 2)
    packet_loss = round(random.uniform(0, 5), 2)

    time.sleep(1)

    return jsonify({
        "source": source,
        "destination": destination,
        "delay_ms": delay_ms,
        "bandwidth_mbps": bandwidth_mbps,
        "snr_db": snr_db,
        "packet_loss": packet_loss
    })

# === 新增：流媒体视频接口 ===
@app.route("/api/video")
def stream_video():
    video_path = os.path.join(os.path.dirname(__file__), "video.mp4")
    if not os.path.exists(video_path):
        return jsonify({"error": "Video file not found"}), 404
    return send_file(video_path, mimetype="video/mp4")

if __name__ == "__main__":
    app.run(debug=True)
