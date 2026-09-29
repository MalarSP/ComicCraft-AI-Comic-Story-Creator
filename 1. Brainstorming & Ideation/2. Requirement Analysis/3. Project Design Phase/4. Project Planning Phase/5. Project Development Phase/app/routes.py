from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import Response, HTMLResponse
from reportlab.pdfgen import canvas
from io import BytesIO

from app.ai.gemini_flash import generate_story, generate_image


router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/")
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "story": None,
            "image": None,
            "topic": ""
        }
    )


@router.post("/generate")
async def generate_comic(
    request: Request,
    topic: str = Form(...)
):

    story = generate_story(topic)

    image = generate_image(topic)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "story": story,
            "image": image,
            "topic": topic
        }
    )


@router.get("/health")
async def health_check():

    return {
        "status": "healthy",
        "application": "ComicCraft"
    }


@router.post("/download-pdf")
async def download_pdf(
    story: str = Form(...)
):

    buffer = BytesIO()

    pdf = canvas.Canvas(buffer)

    pdf.setTitle("ComicCraft Comic")

    pdf.drawString(
        50,
        800,
        "ComicCraft - AI Comic Story Creator"
    )

    y = 770

    for line in story.split("\n"):

        if y < 50:

            pdf.showPage()

            y = 800

        pdf.drawString(
            50,
            y,
            line[:100]
        )

        y -= 20

    pdf.save()

    pdf_data = buffer.getvalue()

    return Response(
        content=pdf_data,
        media_type="application/pdf",
        headers={
            "Content-Disposition":
            "attachment; filename=ComicCraft.pdf"
        }
    )


@router.get(
    "/download-success",
    response_class=HTMLResponse
)
async def download_success():

    return """
    <!DOCTYPE html>

    <html>

    <head>

        <meta charset="UTF-8">

        <title>
            ComicCraft - Download Successful
        </title>

        <style>

            body {

                font-family: Arial, sans-serif;

                background: #f5f5f5;

                text-align: center;

                padding-top: 100px;

            }

            .box {

                background: white;

                width: 550px;

                margin: auto;

                padding: 40px;

                border-radius: 15px;

                box-shadow:
                    0 4px 15px rgba(0,0,0,0.15);

            }

            h1 {

                color: #6a1b9a;

            }

            .success {

                font-size: 60px;

            }

            p {

                font-size: 18px;

            }

            button {

                background: #6a1b9a;

                color: white;

                border: none;

                padding: 12px 25px;

                border-radius: 8px;

                font-size: 16px;

                cursor: pointer;

                margin-top: 20px;

            }

            button:hover {

                background: #4a148c;

            }

        </style>

    </head>


    <body>

        <div class="box">

            <div class="success">
                ✅
            </div>

            <h1>
                Comic Downloaded Successfully!
            </h1>

            <p>
                Your ComicCraft comic has been
                successfully created and downloaded.
            </p>

            <button
                onclick="window.location.href='/'"
            >
                🎨 Create Another Comic
            </button>

        </div>

    </body>

    </html>
    """