from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


load_dotenv()
app = FastAPI()
templates = Jinja2Templates("templates/")
app.mount("/static", StaticFiles(directory="static/"), "static")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

