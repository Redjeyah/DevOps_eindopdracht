from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"message": "DevOps Pipeline eindopdracht"})


@app.route("/health")
def health():
    return jsonify({"status": "goed"})


if __name__ == "__main__":
    app.run(debug=True)
