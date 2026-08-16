from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from pydantic import BaseModel
from pathlib import Path

DATABASE_FILE = Path("database.json")

app = FastAPI(title="CarsWebsite")

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load templates
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "title": "CarsWebsite",
            "message": "Welcome to CarsWebsite!",
        },
    )

@app.get("/api")
async def api():
    return {
        "status": "success",
        "framework": "FastAPI"
    }

if __name__ == "__main__":
    uvicorn.run(
        "main:app",      # filename:app
        host="0.0.0.0",
        port=8000,
        reload=True,     # Automatically reload on code changes
    )