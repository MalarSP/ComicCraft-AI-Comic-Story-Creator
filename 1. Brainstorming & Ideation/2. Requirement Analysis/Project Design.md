# Project Design Phase

## Project Title
ComicCraft – AI Comic Story Creator

## System Architecture

ComicCraft follows a simple web-based architecture.

### Architecture Flow

User
↓
HTML/CSS Frontend
↓
FastAPI Backend
↓
AI Services
↓
Google Gemini + Hugging Face FLUX
↓
Generated Comic Story and Image
↓
Comic Preview
↓
PDF Download

## Main Components

### 1. Frontend
HTML and CSS are used to create the user interface. Jinja2 is used to display the generated content dynamically.

### 2. Backend
FastAPI handles user requests, connects the frontend with the AI services, and manages PDF generation.

### 3. Story Generation
Google Gemini API generates a structured five-panel comic story from the user's topic.

### 4. Image Generation
Hugging Face FLUX generates a colorful comic-style illustration based on the user's topic.

### 5. PDF Generation
ReportLab is used to generate a downloadable PDF containing the generated comic story.

## Data Flow

1. User enters a comic topic.
2. The topic is sent to the FastAPI backend.
3. Gemini generates the comic story.
4. Hugging Face FLUX generates the comic image.
5. The generated content is displayed on the webpage.
6. The user downloads the comic as a PDF.
7. A download success page is displayed.

## Project Structure

```text
ComicCraftAI/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── ai/
│   │   └── gemini_flash.py
│   ├── services/
│   └── routes.py
├── templates/
│   └── index.html
├── .env
└── requirements.txt
