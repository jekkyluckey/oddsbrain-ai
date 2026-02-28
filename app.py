from flask import Flask, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

FOOTBALL_API_KEY = os.getenv("FOOTBALL_API_KEY")

@app.route("/health")
def health():
    return "OK", 200


@app.route("/fixtures")
def get_fixtures():
    url = "https://v3.football.api-sports.io/fixtures"

    querystring = {
        "league": "39",   # Premier League
        "season": "2023"
    }

    headers = {
        "x-apisports-key": FOOTBALL_API_KEY
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/test-key")
def test_key():
    return {"key": FOOTBALL_API_KEY}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
