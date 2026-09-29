# Project Development Phase

## Project Title
ComicCraft – AI Comic Story Creator

## Development Overview

The ComicCraft application was developed using Python and FastAPI. AI services were integrated to generate comic stories and comic-style images.

## Backend Development

FastAPI was used to create the backend application and handle user requests.

The backend includes:

- Application initialization
- Web routes
- Comic story generation
- Image generation
- PDF generation
- Download success page

## AI Integration

### Google Gemini

Google Gemini is used to generate a structured five-panel comic story from the topic provided by the user.

### Hugging Face FLUX

Hugging Face FLUX is used to generate a colorful comic-style image based on the user's topic.

## Frontend Development

HTML and CSS were used to create the ComicCraft interface.

The interface provides:

- ComicCraft title
- Topic input field
- Generate Comic button
- Generated story display
- Generated image display
- PDF download button

## PDF Generation

ReportLab is used to create a downloadable PDF containing the generated comic story.

## Development Workflow

User Input
↓
FastAPI Backend
↓
Gemini Story Generation
↓
Hugging Face Image Generation
↓
Comic Preview
↓
PDF Generation
↓
Download Success Page

## Development Result

The developed application successfully provides an integrated workflow for generating an AI-based comic story and comic-style image from a user-provided topic.
