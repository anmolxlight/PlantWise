# PlantWise: AI-Powered Plant Medicine Advisor

## About
PlantWise is an AI-powered application developed as a module for Smart India Hackathon (SIH) 2024. This tool helps users identify potential natural remedies for various health symptoms based on traditional herbal and Ayurvedic medicine knowledge.

The application processes user-reported symptoms, analyzes them using AI, and provides tailored plant-based remedy suggestions while also warning about things to avoid for the identified health conditions.

## Features
- **Symptom Analysis**: Users can input their health symptoms in natural language
- **AI-Powered Recommendations**: Utilizes Google's Gemini AI to analyze symptoms and suggest remedies
- **Plant-Based Solutions**: Focuses on traditional herbal and Ayurvedic treatments
- **Precautionary Advice**: Includes things to avoid for better health outcomes

## Tech Stack
- **Backend**: Python with Flask
- **AI**: Google Gemini 2.0 Flash model
- **Frontend**: HTMl, CSS

## Setup Instructions

### Local Development

1. Clone the repository:
   ```
   git clone https://github.com/anmolxlight/PlantWise
   cd PlantWise
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory by copying the env.example file:
   ```
   # Windows
   copy env.example .env
   
   # Mac/Linux
   cp env.example .env
   ```
   
   Or create it manually with the following content:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```
   Replace `your_api_key_here` with your actual Google Gemini API key.

4. Run the application:
   ```
   python app.py
   ```

5. Access the application at `http://localhost:5000`
