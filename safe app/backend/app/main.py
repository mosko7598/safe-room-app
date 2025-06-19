from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import users, safe_rooms  # נוסיף גם auth אם נרצה
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import os

app = FastAPI(
    title="SAFE-ROOM",
    description="מערכת ניהול ממ״דים חכמה",
    version="1.0.0"
)

FRONTEND_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../frontend"))
app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")

# הגדרת CORS – לאפשר קריאות מה-frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # אפשר להגביל ל-origin ספציפי בהמשך
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# חיבור ה-routers
app.include_router(users.router)
app.include_router(safe_rooms.router)
# app.include_router(auth.router)  ← רק אם נוסיף בעתיד

@app.get("/")
def root():
    return {"message": "SAFE-ROOM API is running"}

from fastapi.responses import RedirectResponse

@app.get("/app")
def redirect_to_app_index():
    return RedirectResponse(url="/app/")
