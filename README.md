# PlantWise 🌱

**AI-Powered Herbal Medicine Advisor**

PlantWise is an AI-powered application developed for Smart India Hackathon (SIH) 2024. Describe your symptoms and get plant-based remedy suggestions rooted in traditional herbal and Ayurvedic medicine knowledge.

**Live demo:** [plantwisebackend.onrender.com](https://plantwisebackend.onrender.com)

---

## Features

- **Symptom Analysis** — Input your symptoms in natural language
- **AI-Powered Recommendations** — Google Gemini 2.5 Flash analyzes symptoms and suggests remedies
- **Plant-Based Solutions** — Traditional herbal and Ayurvedic treatments
- **Precautionary Advice** — Includes things to avoid for better outcomes
- **Dark/Light Mode** — Automatic system preference detection with manual toggle
- **Mobile Responsive** — Works on all screen sizes

## Tech Stack

| Layer   | Technology                              |
| ------- | --------------------------------------- |
| Backend | Python 3.10+ · Flask 3.1                |
| AI      | Google Gemini 2.5 Flash API             |
| Frontend | HTML5 · CSS3 (custom properties) · Vanilla JS |
| Hosting | Render (backend) · GitHub Pages / Render (frontend) |

## Setup

### Prerequisites
- Python 3.10 or later
- A [Google Gemini API key](https://aistudio.google.com/app/apikey)

### Local Development

```bash
# 1. Clone
git clone https://github.com/anmolxlight/PlantWise.git
cd PlantWise

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure API key
cp .env.example .env
# Edit .env and set your GEMINI_API_KEY

# 5. Run
python app.py

# 6. Open http://localhost:5000
```

### Environment Variables

| Variable        | Required | Description                  |
| --------------- | -------- | ---------------------------- |
| `GEMINI_API_KEY` | Yes      | Google Gemini API key        |
| `PORT`          | No       | Server port (default: 5000)  |
| `FLASK_DEBUG`   | No       | Set to `1` for debug mode    |

## API

### `POST /get_remedy`

Analyze symptoms and get herbal remedy suggestions.

**Request:**
```json
{ "symptoms": "headache, fatigue, cough" }
```

**Response:**
```json
{
  "response": "Possible Conditions\n...\nHerbal Remedies\n...\nThings to Avoid\n..."
}
```

### `GET /health`

Health check endpoint.

## Deployment

The app is designed for [Render](https://render.com). Use the following settings:

- **Runtime:** Python 3
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`

## Project Structure

```
PlantWise/
├── app.py               # Flask backend
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variable template
├── static/
│   ├── index.html       # Frontend (single-page app)
│   └── robots.txt       # Crawler rules
└── README.md
```

## Disclaimer

This application is for informational purposes only. The herbal remedies suggested are based on traditional knowledge and AI analysis. Always consult a qualified healthcare professional before trying any treatment. Never disregard professional medical advice or delay in seeking it based on information from this app.

## License

MIT
