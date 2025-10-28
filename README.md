# 🧠 Anviro — AI Text Sentiment & Summary API

Anviro is a lightweight **Flask-based AI API** that performs **sentiment analysis** and **text summarization** using Hugging Face Transformers and OpenRouter API.

---

## 🚀 Features

- 🔍 Sentiment analysis using **DistilBERT**
- 📝 Smart summarization via **OpenRouter API**
- ⚡ Lightweight Flask backend
- 🧠 Ready for integration with frontend or mobile apps

---

## 🛠️ Installation Guide

### 1. Clone the Repository
```bash
git clone https://github.com/Touseeq20/anviro.git
cd anviro
```

### 2. Create a Virtual Environment
```bash
python -m venv .venv
```

### 3. Activate the Environment
#### For Windows (PowerShell)
```bash
.venv\Scripts\activate
```
#### For Mac/Linux
```bash
source .venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install flask transformers requests torch
```

---

## 🔑 Setup OpenRouter API Key

1. Visit [OpenRouter.ai](https://openrouter.ai/keys)
2. Copy your API key  
3. Open **app.py** and replace the placeholder:

```python
OPENROUTER_API_KEY = "sk-or-v1-REPLACE-WITH-YOUR-KEY"
```

with your real API key.

---

## ▶️ Run the Flask App
```bash
python app.py
```

The app will start at:

```
http://127.0.0.1:8000/
```

---

## 📡 API Usage

### ✅ Check Server Status
**GET**
```
http://127.0.0.1:8000/
```

**Response:**
```json
{
  "message": "✅ Flask Smart Text Analyzer is running!",
  "endpoints": {
    "POST /analyze": "Analyze sentiment and summarize text"
  }
}
```

---

### 🧾 Analyze Text
**POST**
```
http://127.0.0.1:8000/analyze
```

**Request Body:**
```json
{
  "text": "I love this new AI model! It's super fast and accurate."
}
```

**Response:**
```json
{
  "sentiment": "positive",
  "confidence": 0.999,
  "summary": "The user is happy about the AI model’s speed and accuracy."
}
```

---

## 🧩 Project Structure

```
anviro/
├── app.py                # Main Flask application
├── requirements.txt      # Dependencies (optional)
└── README.md             # Documentation
```

---

## 👨‍💻 Author
**Muhammad Touseeq**  
AI Engineer | Python Developer | NLP & Agentic AI Researcher  
📧 [Contact Me](mailto:touseeq20@gmail.com)

---

## 📜 License
This project is licensed under the **MIT License** — feel free to use, modify, and distribute.
