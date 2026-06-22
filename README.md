# Audio Summarizer

An AI-powered web application that generates concise summaries from uploaded audio files. The application transcribes audio using Groq's Speech-to-Text API and generates structured summaries using a Large Language Model (LLM).

---

## Features

* Upload audio files (`.mp3`, `.wav`, `.m4a`, `.aac`)
* Automatic speech-to-text transcription
* AI-powered summarization
* Structured output format:

  * Title
  * Brief Overview
  * Key Points
  * Conclusion
* FastAPI backend
* Responsive web interface using HTML/CSS
* Cloud deployment using Render

---

## Architecture Overview

```text
┌──────────────────────┐
│      User Browser    │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ FastAPI Application  │
│     (Render)         │
└──────────┬───────────┘
           │
           │ Upload Audio
           ▼
┌──────────────────────┐
│ Temporary File Store │
│      (/tmp)          │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  Groq Speech API     │
│ whisper-large-v3     │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Transcript Generated │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ LangChain Pipeline   │
│ Prompt Engineering   │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  Groq LLM Model      │
│  Text Summarization  │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Structured Summary   │
└──────────────────────┘
```

---

## Tech Stack

### Backend

* FastAPI
* Uvicorn
* Python

### AI & NLP

* Groq Speech-to-Text API
* Groq LLM
* LangChain
* Prompt Engineering

### Frontend

* HTML
* CSS
* Jinja2 Templates

### Deployment

* Render

---

## APIs & Services Used

### 1. Groq Speech-to-Text API

Used for audio transcription.

Model:

```python
whisper-large-v3
```

Purpose:

* Converts uploaded audio into text transcript.

---

### 2. Groq LLM API

Used for text summarization.

Example Models:

```python
openai/gpt-oss-120b
```

Purpose:

* Generates concise and structured summaries.

---

### 3. LangChain

Used for:

* Prompt management
* LLM orchestration
* Output parsing

Components:

```python
ChatPromptTemplate
StrOutputParser
```

---

## Project Structure

```text
english_assignment/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/mishraatharva/english_assignment.git

cd english_assignment
```

---

### Create Virtual Environment

Windows:

```bash
python -m venv venv

venv\Scripts\activate
```

Linux/Mac:

```bash
python -m venv venv

source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=openai/gpt-oss-120b
```

---

## Run Locally

```bash
uvicorn app:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

---

## Workflow

### Step 1

User uploads an audio file.

### Step 2

FastAPI receives the file and stores it temporarily.

### Step 3

Audio is sent to Groq Speech API.

### Step 4

Speech API generates transcript.

### Step 5

Transcript is passed to LangChain.

### Step 6

LangChain sends prompt to Groq LLM.

### Step 7

LLM generates:

* Title
* Overview
* Key Points
* Conclusion

### Step 8

Summary is displayed in the web interface.

---

## Deployment on Render

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
uvicorn app:app --host 0.0.0.0 --port $PORT
```

### Environment Variables

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=openai/gpt-oss-120b
```

---

## Future Improvements

* Multi-language Support
* Audio URL Input
* Sentiment Analysis
* Implimenting more advance summarization techniques like Map-Reduce Summarization, Refine Chain Summarization for handling large audio  and more accurate and usefull summary.

---

## Author

Atharva Mishra

AI / Machine Learning Engineer

GitHub:
https://github.com/mishraatharva

LinkedIn:
https://www.linkedin.com/in/atharva-mishra
