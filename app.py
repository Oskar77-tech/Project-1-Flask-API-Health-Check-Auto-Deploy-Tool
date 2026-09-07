from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "API Health Check",
        "status": "running"
    })

@app.route("/health")
def health():
    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/posts/1",
            timeout=5
        )

        return jsonify({
            "status": "healthy",
            "target_status": response.status_code
        })

    except Exception as e:
        return jsonify({
            "status": "unhealthy",
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)