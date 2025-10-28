# 🧠 Smart Text Analyzer (Flask + Transformers + OpenRouter)

This project is a **Flask-based AI text analyzer** that performs:
- 🪞 Sentiment Analysis (Positive / Negative)
- ✍️ Text Summarization using OpenRouter API (GPT/Mistral)

---

## 🚀 Features
- Real-time text analysis via REST API  
- Sentiment analysis powered by **Hugging Face Transformers**
- AI-based summarization using **OpenRouter**
- JSON API response for easy integration with web or mobile apps

---

## 🛠️ Installation Guide

### 1. Clone this repository
```bash
git clone https://github.com/Touseeq20/anviro.git
cd anviro
2. Create a virtual environment
bash
Copy code
python -m venv .venv
3. Activate the environment
For Windows (PowerShell)
bash
Copy code
.venv\Scripts\activate
For Mac/Linux
bash
Copy code
source .venv/bin/activate
4. Install dependencies
bash
Copy code
pip install flask transformers requests torch
🔑 Setup OpenRouter API Key
Go to https://openrouter.ai/keys

Copy your API key

Open app.py and replace:

python
Copy code
OPENROUTER_API_KEY = "sk-or-v1-REPLACE-WITH-YOUR-KEY"
with your real key.

▶️ Run the Flask App
bash
Copy code
python app.py
Your app will start on:

cpp
Copy code
http://127.0.0.1:8000/
📡 API Usage
✅ Check if server is running
GET http://127.0.0.1:8000/

Response:

json
Copy code
{
  "message": "✅ Flask Smart Text Analyzer is running!",
  "endpoints": {
    "POST /analyze": "Analyze sentiment and summarize text"
  }
}
🧾 Analyze Text
POST http://127.0.0.1:8000/analyze

Request Body:

json
Copy code
{
  "text": "I love this new AI model! It's super fast and accurate."
}
Response:

json
Copy code
{
  "sentiment": "positive",
  "confidence": 0.999,
  "summary": "The user is happy about the AI model’s speed and accuracy."
}
