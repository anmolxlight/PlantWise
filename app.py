from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import requests
import re
import json

app = Flask(__name__)
CORS(app)

GEMINI_API_KEY = 'AIzaSyB0-aeyiJ5qEygH0FB4uDV3I-MPWUzCDog'
GEMINI_URL = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}'

def get_ai_response(prompt):
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }
    try:
        response = requests.post(GEMINI_URL, headers=headers, data=json.dumps(data))
        result = response.json()
        return result['candidates'][0]['content']['parts'][0]['text'].strip()
    except Exception as e:
        return f"An error occurred: {e}"

def clean_input(user_input):
    user_input = re.sub(r'[^a-zA-Z, ]', '', user_input).lower().strip()
    return user_input

def remove_markdown(text):
    text = re.sub(r'\*\*', '', text)
    text = re.sub(r'[_]', '', text)
    text = re.sub(r'[`]', '', text)
    text = re.sub(r'~', '', text)
    return text

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/get_remedy', methods=['POST'])
def get_remedy():
    data = request.json
    symptoms = data.get('symptoms', '')

    cleaned_input = clean_input(symptoms)
    if not cleaned_input:
        return jsonify({"error": "Invalid input. Please describe your symptoms properly."}), 400

    user_symptoms = [symptom.strip() for symptom in cleaned_input.split(",")]

    ai_prompt = f"""
    The user has the following symptoms: {', '.join(user_symptoms)}.
    Identify potential diseases or health conditions associated with these symptoms.
    Suggest concise plant-based herbal medicines or mixtures traditionally used in herbal or Ayurvedic treatments for these conditions.
    Include a brief list of things to avoid while dealing with these conditions.
    No additional details or descriptions.
    """

    ai_response = get_ai_response(ai_prompt)
    ai_response = remove_markdown(ai_response)

    return jsonify({"response": ai_response})

if __name__ == '__main__':
    app.run(debug=True)
