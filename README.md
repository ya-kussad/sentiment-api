# 🧠 Sentiment Analysis API using Ollama & LLaMA3

This project is a simple, self-hosted sentiment analysis REST API that uses an open-source LLM (LLaMA3 via Ollama) and exposes a web interface to input text and analyze its sentiment.

---

## 🚀 Features

- Uses **Ollama** with the **LLaMA3 3B** model
- Accepts text input in English or Arabic
- Returns sentiment as: `Positive`, `Neutral`, or `Negative`
- Simple web interface (HTML form)
- Self-contained using Docker

---

## 📦 Requirements

- Docker installed → [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose → comes with Docker Desktop or can be installed separately

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/sentiment-api.git
cd sentiment-api
```
### 2. Pull the Ollama Docker image
```bash
docker pull ollama/ollama
```
### 3. Start Ollama container and download model
```bash
# Start Ollama in the background
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

# Pull the LLaMA3 model (3B)
docker exec -it ollama ollama pull llama3.2:3b
```
### 4. Build and run the sentiment API

```bash
#docker rm -f ollama
docker-compose up --build
```
This starts sentiment-api at http://localhost:8000/

### Usage:

### 1. Using Web Interface:
Open your browser and go to:
```bash
http://localhost:8000/
```
- Enter any short text summary (~150 characters)

- Click "Analyze" to get the sentiment

- Click "Clear" to reset the form

### 2. API Usage
```bash
curl -X POST http://localhost:8000/generate \
     -H "Content-Type: application/json" \
     -d '{"prompt": "I love this product!"}'
```

###  Model & Hardware Considerations

- Model Used: llama3.2:3b via Ollama

- Language Support: Good for both English and Arabic

- Inference: Runs reasonably on CPU but faster with GPU

### Project Structure
```php
sentiment-api/
├── app/
│   ├── main.py              # FastAPI app with sentiment endpoint
│   ├── static/
│   │   └── index.html       # Web interface
│   └── requirements.txt
├── Dockerfile               # Builds sentiment-api container
├── docker-compose.yml       # Orchestrates ollama + API
└── README.md

