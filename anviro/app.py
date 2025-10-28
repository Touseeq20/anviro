


from flask import Flask, request, jsonify
from transformers import pipeline
import requests

app = Flask(__name__)

# ----------------------------
# Load Sentiment Model
# ----------------------------
sentiment_model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# ----------------------------
# OpenRouter API Setup
# ----------------------------
OPENROUTER_API_KEY = "sk-or-v1-2c7e3126"  # ⚠️ Replace with your own key

def summarize_text_with_openrouter(text):
    """Uses OpenRouter API to summarize input text."""
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "model": "openai/gpt-3.5-turbo",  # You can change to "mistralai/mistral-7b-instruct"
        "messages": [
            {"role": "system", "content": "Summarize this text in one short sentence."},
            {"role": "user", "content": text}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        summary = response_json["choices"][0]["message"]["content"]
    except Exception as e:
        summary = f"Error generating summary: {e}"

    return summary


# ----------------------------
# Root route (for testing)
# ----------------------------
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "✅ Flask Smart Text Analyzer is running!",
        "endpoints": {
            "POST /analyze": "Analyze sentiment and summarize text"
        }
    })


# ----------------------------
# Main Analysis Endpoint
# ----------------------------
@app.route("/analyze", methods=["POST"])
def analyze_text():
    """Main endpoint for text analysis"""
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Please provide 'text' in JSON body."}), 400

    text = data["text"]

    # Sentiment Analysis
    sentiment_result = sentiment_model(text)[0]
    sentiment_label = sentiment_result["label"].lower()
    sentiment_score = round(sentiment_result["score"], 3)

    # Summarization (via OpenRouter)
    summary = summarize_text_with_openrouter(text)

    # JSON response
    result = {
        "sentiment": sentiment_label,
        "confidence": sentiment_score,
        "summary": summary
    }

    return jsonify(result)


# ----------------------------
# Run Server
# ----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)


