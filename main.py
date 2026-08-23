from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from pydantic import BaseModel
from db_utils import load_item
from pathlib import Path

DATABASE_FILE = Path("database.json")

app = FastAPI(title="CarsWebsite    ")

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


@app.get("/electric-cars", response_class=HTMLResponse)
async def electric_cars(request: Request):
    electric_cars = load_item("electric_cars")
    return templates.TemplateResponse(
        "electric_cars.html",
        {
            "request": request,
            "title": "Electric Cars",
            "message": "Welcome to Electric Cars page!",
            "electric_cars": electric_cars
        },
    )


@app.get("/sports-cars", response_class=HTMLResponse)
async def sports_cars(request: Request):
    sports_cars = load_item("sports_cars")
    return templates.TemplateResponse(
        "sports_cars.html",
        {
            "request": request,
            "title": "Sports Cars",
            "message": "Welcome to Sports Cars page!",
            "sports_cars": sports_cars
        },
    )

@app.get("/luxury-cars", response_class=HTMLResponse)
async def luxury_cars(request: Request):
    luxury_cars = load_item("luxury_cars")
    return templates.TemplateResponse(
        "luxury_cars.html",
        {
            "request": request,
            "title": "Luxury Cars",
            "message": "Welcome to Luxury Cars page!",
            "luxury_cars": luxury_cars
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