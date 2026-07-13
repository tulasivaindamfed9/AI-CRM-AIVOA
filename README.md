# AI-First CRM HCP Module

An AI-powered CRM application for Healthcare Professional (HCP) interaction logging using React, Redux, FastAPI, LangGraph, Groq LLM, and PostgreSQL.

---

## Objective

This application allows field representatives to log and update HCP interactions using a conversational AI interface instead of manually filling forms.

The AI extracts structured information from natural language, stores it in PostgreSQL, and automatically updates the interaction details form.

---

## Features

- AI-powered interaction logging
- AI-powered interaction editing
- Read-only interaction details form
- Conversational chat interface
- Automatic date and time generation
- Loading indicator
- Toast notifications
- PostgreSQL database integration

---

## Tech Stack

### Frontend

- React
- Redux Toolkit
- Bootstrap 5
- Axios
- React Toastify

### Backend

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL

### AI

- LangGraph
- Groq API
- llama-3.1-8b-instant

---

## Project Structure

```
AI-CRM/
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── backend/
│   ├── app/
│   ├── requirements.txt
│   └── main.py
```

---

## Installation

### Backend

```bash
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

---

### Frontend

```bash
cd frontend

npm install

npm run dev
```

---


## API Endpoints

### Log Interaction

```
POST /interaction/log
```

Logs a new HCP interaction using AI.

---

### Edit Interaction

```
PUT /interaction/edit
```

Updates the latest interaction based on natural language instructions.

---

### Latest Interaction

```
GET /interaction/latest
```

Returns the latest interaction stored in PostgreSQL.

---

## AI Workflow

```
User Chat
      │
      ▼
React UI
      │
      ▼
FastAPI
      │
      ▼
LangGraph
      │
      ▼
Groq LLM (Gemma2-9B-IT)
      │
      ▼
Structured JSON
      │
      ▼
PostgreSQL
      │
      ▼
Redux
      │
      ▼
Interaction Details Form
```

---

## Example

### Log Interaction

```
Today I met Dr. Ramesh at Apollo Hospital. We discussed diabetes medicine. I shared a product brochure and distributed three sample packs. The doctor showed interest in prescribing the medicine. I will follow up next week.
```

---

### Edit Interaction

```
Change the sentiment to Neutral and update the follow up actions to schedule another meeting after two weeks.
```

---

## Assignment Requirements Covered

- React UI with Redux
- FastAPI backend
- LangGraph integration
- Groq LLM integration
- PostgreSQL database
- AI-powered Log Interaction
- AI-powered Edit Interaction
- Conversational AI interface

---

## Author

Tulasi Vaindam
