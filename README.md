# Sentiment Analysis API using Ollama & LLaMA3.2 3B

This project is a simple, self-hosted sentiment analysis REST API that uses an open-source LLM (LLaMA3 via Ollama) and has a basic web interface to input text in Arabic and English and analyze its sentiment.

---

## Features

- Uses **Ollama** with the **LLaMA3.2 3B** model
- Accepts text input in English or Arabic
- Returns sentiment as: `Positive`, `Neutral`, or `Negative`
- Simple web interface (HTML form)
- Self-contained using Docker

---

## Requirements

- Docker installed → [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose → comes with Docker Desktop or can be installed separately using:
```bash
sudo apt-get install docker-compose-plugin ##for linux
```

---

## Setup Instructions

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
     -d '{"prompt": "تواصل العميل مع خدمة العملاء لأنه كان لدبه مشكلة مع جهازه وهذه المشكلة لم تعالج حتى بعد عدة محاولات."}'
```

###  Model & Hardware Considerations

- Model Used: llama3.2:3b via Ollama
    - Ollama is an open-source framework that is easy use and is continously maintained and updated as of the dat of this task.
    - It is easy to setup and docker which allows creating a ready-to-use containter for projects. It has light docker images, and it is optimized for use on laptops and small servers.
    - It supports most open-source LLMs, and it optimizes the usage of quantized models on CPU.
    - It has support to run models on both GPU & CPU.

    - Llama3.2 3B is a model that is trained on Meta's multi-lingual dataset therefore it contains Arabic and English. Its size offers a balance between performance and usability on mulltiple hardwares.
    - Llama3 models have shown great perfromance on various NLP tasks.

- Language Support: Good for both English and Arabic

- Inference: Runs reasonably on CPU but faster with GPU. Current setup is made to run on CPU.
    - With more resources, I would have used Llama 3.2 8B model which has shown much better performance pn various Arabic (https://huggingface.co/blog/leaderboard-arabic) and English datasets.

### Project Structure
```php
sentiment-api/
├── app/
│   ├── main.py              # FastAPI app with sentiment endpoint
│   ├── static/
│   │   └── index.html       # Web interface
│   └── requirements.txt
├── Dockerfile               # Builds sentiment-api container
├── docker-compose.yml       
└── README.md

