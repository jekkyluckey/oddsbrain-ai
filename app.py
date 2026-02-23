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
    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"

    querystring = {
        "league": "39",   # English Premier League
        "season": "2023"
    }

    headers = {
        "X-RapidAPI-Key": FOOTBALL_API_KEY,
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring, timeout=10)
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
