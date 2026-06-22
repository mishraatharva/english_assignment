from fastapi import FastAPI, UploadFile, File, HTTPException, Request
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from groq import Groq
import tempfile
import shutil
import uuid
import os

load_dotenv()

app = FastAPI()

UPLOAD_DIR = tempfile.gettempdir()

templates = Jinja2Templates(directory="templates")

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

llm = ChatGroq(
    model=os.environ.get("GROQ_MODEL"),
    api_key=os.environ.get("GROQ_API_KEY"))


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_transcript(audio_file_path):
    with open(audio_file_path, "rb") as file:
        transcription = client.audio.transcriptions.create(
            file=file,
            model="whisper-large-v3"
        )

    return transcription.text


def generate_summary(transcript):
    prompt = ChatPromptTemplate.from_template(
        """
        You are a professional summarization assistant.

        Summarize the following transcript.

        Requirements:
            1. Keep the summary under 25% of the transcript length.
            2. Do not add information that is not explicitly stated.
            3. Generate:
               - Title
               - Brief Overview (3-4 sentences)
               - Key Points (bullet format)
               - Conclusion (2-3 sentences)
            4. Avoid tables.
            5. Avoid action items unless explicitly mentioned.
            6. Avoid repeating information.
            7. Use concise language.

        Transcript:
        {transcript}
        """
    )

    chain = prompt | llm | StrOutputParser()

    summary = chain.invoke({
        "transcript": transcript
    })

    print(summary)

    return summary
    
    
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
        "summary": None
        }
    )


@app.post("/", response_class=HTMLResponse)
async def upload_audio(
    request: Request,
    audio: UploadFile = File(...)
):

    if not audio.filename.endswith(
        (".mp3", ".wav", ".m4a", ".aac")
    ):
        raise HTTPException(
            status_code=400,
            detail="Unsupported audio format"
        )

    file_path = os.path.join(
        UPLOAD_DIR,
        f"{uuid.uuid4()}_{audio.filename}"
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(audio.file, buffer)

    transcript = generate_transcript(file_path)

    summary = generate_summary(transcript)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "summary": summary
        }
    )