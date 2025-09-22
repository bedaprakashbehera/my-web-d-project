from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Demo credentials
USERNAME = "Krishna@1234"
PASSWORD = "1234"

@app.route("/api/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username", "").strip()
    password = data.get("password", "").strip()
    if username == USERNAME and password == PASSWORD:
        return jsonify({"success": True, "message": "Login successful!", "name": "Bedaprakash Behera"})
    return jsonify({"success": False, "message": "Invalid credentials."}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
