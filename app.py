import json
import os
import re
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv
import requests

load_dotenv()

app = Flask(__name__)
CORS(app)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY environment variable is not set. "
        "Create a .env file by copying .env.example or refer to README.md."
    )

# Updated to Gemini 2.5 Flash — faster than 2.0 Flash with better quality
GEMINI_MODEL = "gemini-2.5-flash"
GEMINI_URL = (
    f"https://generativelanguage.googleapis.com/v1beta/models/"
    f"{GEMINI_MODEL}:generateContent?key={GEMINI_API_KEY}"
)

SYSTEM_PROMPT = (
    "You are PlantWise, an AI herbal medicine advisor. "
    "When given health symptoms, identify potential conditions and suggest "
    "traditional plant-based or Ayurvedic remedies. "
    "Always include things to avoid. "
    "Format your answer with clear sections: "
    "'Possible Conditions', 'Herbal Remedies', and 'Things to Avoid'. "
    "Keep responses concise, factual, and safe — include a disclaimer "
    "that this is not medical advice and to consult a doctor."
)


def get_ai_response(prompt: str) -> str:
    """Send prompt to Gemini API and return the response text."""
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "systemInstruction": {"parts": [{"text": SYSTEM_PROMPT}]},
        "generationConfig": {
            "temperature": 0.4,
            "maxOutputTokens": 1024,
        },
    }
    headers = {"Content-Type": "application/json"}

    try:
        resp = requests.post(
            GEMINI_URL,
            headers=headers,
            data=json.dumps(payload),
            timeout=30,
        )
        resp.raise_for_status()
        result = resp.json()

        candidates = result.get("candidates")
        if candidates:
            parts = candidates[0].get("content", {}).get("parts", [])
            if parts and "text" in parts[0]:
                return parts[0]["text"].strip()
            return "No text content in response."

        error_info = result.get("error", {})
        return f"Gemini API error: {error_info.get('message', 'Unknown error')}"

    except requests.exceptions.Timeout:
        return "Request timed out. Please try again."
    except requests.exceptions.HTTPError as e:
        status = e.response.status_code
        try:
            detail = e.response.json().get("error", {}).get("message", "")
        except (json.JSONDecodeError, ValueError):
            detail = e.response.text[:200]
        return f"API error ({status}): {detail}"
    except requests.exceptions.ConnectionError:
        return "Could not connect to the API. Check your internet connection."
    except Exception as e:
        return f"Unexpected error: {str(e)}"


def clean_input(user_input: str) -> str:
    """Strip invalid characters and normalize whitespace."""
    cleaned = re.sub(r"[^a-zA-Z, ]", "", user_input).strip().lower()
    # Collapse multiple spaces/commas
    cleaned = re.sub(r"\s+", " ", cleaned)
    cleaned = re.sub(r",\s*,", ",", cleaned)
    return cleaned


def remove_markdown(text: str) -> str:
    """Strip basic markdown formatting from Gemini output."""
    return re.sub(r"(\*\*|__|~~|`|#)", "", text)


@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/health")
def health():
    return jsonify({"status": "ok", "model": GEMINI_MODEL})


@app.route("/get_remedy", methods=["POST"])
def get_remedy():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Request must contain valid JSON."}), 400

    symptoms = (data.get("symptoms") or "").strip()
    cleaned_input = clean_input(symptoms)

    if not cleaned_input:
        return jsonify({"error": "Please describe your symptoms properly."}), 400

    user_symptoms = [s.strip() for s in cleaned_input.split(",") if s.strip()]

    ai_prompt = (
        f"The user reports the following symptoms: {', '.join(user_symptoms)}.\n\n"
        "Analyze these symptoms and identify potential conditions. "
        "Suggest plant-based herbal medicines or Ayurvedic treatments. "
        "List things to avoid while managing these conditions.\n\n"
        "Format your answer with these sections:\n"
        "**Possible Conditions**\n"
        "**Herbal Remedies**\n"
        "**Things to Avoid**\n"
        "**Disclaimer**"
    )

    ai_response = get_ai_response(ai_prompt)
    cleaned_response = remove_markdown(ai_response)

    return jsonify({"response": cleaned_response})


@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    debug = os.getenv("FLASK_DEBUG", "0") == "1"
    app.run(host="0.0.0.0", port=port, debug=debug)
