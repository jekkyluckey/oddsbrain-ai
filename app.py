from flask import Flask, jsonify
import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

app = Flask(__name__)

FOOTBALL_API_KEY = os.getenv("FOOTBALL_API_KEY")

@app.route("/health")
def health():
    return "OK", 200


@app.route("/fixtures")
def get_fixtures():

    # Automatically calculate season (season starts in August)
    current_year = datetime.now().year
    current_month = datetime.now().month

    if current_month < 8:
        season = current_year - 1
    else:
        season = current_year

    url = "https://v3.football.api-sports.io/fixtures"

    querystring = {
        "league": "39",   # Premier League
        "season": str(season)
    }

    headers = {
        "x-apisports-key": FOOTBALL_API_KEY
    }

    if not FOOTBALL_API_KEY:
        return jsonify({"error": "API key not set"}), 500

    try:
        response = requests.get(url, headers=headers, params=querystring)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/test-key")
def test_key():
    return {"key_loaded": bool(FOOTBALL_API_KEY)}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
