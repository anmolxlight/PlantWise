# PlantWise: AI-Powered Plant Medicine Advisor

## About
PlantWise is an AI-powered application developed as a module for Smart India Hackathon (SIH) 2024. This tool helps users identify potential natural remedies for various health symptoms based on traditional herbal and Ayurvedic medicine knowledge.

**Website:** https://sites.google.com/view/plantwise/virtual-garden

The application processes user-reported symptoms, analyzes them using AI, and provides tailored plant-based remedy suggestions while also warning about things to avoid for the identified health conditions.

## Features
-   **Symptom Analysis**: Users can input their health symptoms in natural language.
-   **AI-Powered Recommendations**: Utilizes Google's Gemini AI to analyze symptoms and suggest remedies.
-   **Plant-Based Solutions**: Focuses on traditional herbal and Ayurvedic treatments.
-   **Precautionary Advice**: Includes things to avoid for better health outcomes.

## Tech Stack
-   **Backend**: Python with Flask
-   **AI**: Google Gemini 2.0 Flash model
-   **Frontend**: HTML, CSS

## Setup Instructions

### Local Development

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/anmolxlight/PlantWise](https://github.com/anmolxlight/PlantWise)
    cd PlantWise
    ```

2.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Create a `.env` file:**
    Create a `.env` file in the root directory by copying the `env.example` file:
    ```bash
    # On Windows
    copy env.example .env
    
    # On Mac/Linux
    cp env.example .env
    ```
    Alternatively, you can create it manually with the following content:
    ```
    GEMINI_API_KEY=your_api_key_here
    ```
    **Important:** Replace `your_api_key_here` with your actual Google Gemini API key. You can obtain an API key from [Google AI Studio](https://aistudio.google.com/app/apikey) or the Google Cloud Console.

4.  **Run the application:**
    ```bash
    python app.py
    ```

5.  **Access the application:**
    Open your web browser and navigate to `http://localhost:5000`.
