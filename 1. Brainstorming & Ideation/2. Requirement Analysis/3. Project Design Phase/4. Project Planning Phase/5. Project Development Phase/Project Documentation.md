# Project Documentation

## Project Title
ComicCraft – AI Comic Story Creator

## Abstract

ComicCraft is an AI-powered web application designed to create short comic stories and comic-style illustrations from a user-provided topic. The application uses Google Gemini for story generation and Hugging Face FLUX for image generation. FastAPI is used as the backend framework, while HTML, CSS, and Jinja2 are used to create the user interface. The generated comic story can also be downloaded as a PDF using ReportLab.

## Introduction

Creating a comic traditionally requires story writing, character development, illustration, and design skills. ComicCraft simplifies this process by using Generative AI to automatically create comic content from a simple topic provided by the user.

## Objectives

- Generate creative comic stories using AI.
- Generate comic-style illustrations.
- Provide a simple and user-friendly interface.
- Allow users to download the generated story as a PDF.
- Demonstrate the practical use of Generative AI.

## Technologies Used

- Python
- FastAPI
- HTML
- CSS
- Jinja2
- Google Gemini API
- Hugging Face FLUX
- ReportLab

## System Workflow

User enters a topic → Gemini generates the comic story → Hugging Face FLUX generates the comic image → Results are displayed → User downloads the comic as PDF.

## Benefits

- Saves time in comic creation.
- Easy for beginners to use.
- Combines AI text and image generation.
- Provides a simple web-based experience.
- Supports PDF export.

## Limitations

- AI-generated content depends on the quality of the input topic.
- Internet access is required for API-based generation.
- API availability and usage limits may affect generation.
- Generated images may not always perfectly match the story.

## Future Enhancements

- Generate separate images for each comic panel.
- Add character customization.
- Add different comic styles.
- Include generated images inside the PDF.
- Add multilingual comic generation.
- Deploy the application online.

## Conclusion

ComicCraft demonstrates how Generative AI can be used to simplify creative content generation. By combining AI-based story and image generation with a web application, users can create comic content from a simple topic and export the result as a PDF.
