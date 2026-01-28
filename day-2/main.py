from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine
from models.base import Base
from routers import users  # Import the users router
from config import settings

# -------------------------
# Create FastAPI instance
# -------------------------
app = FastAPI(
    title="FastAPI PostgreSQL Example",
    description="A clean, production-ready FastAPI project with PostgreSQL",
    version="1.0.0",
    debug=settings.DEBUG
)

# -------------------------
# CORS middleware (optional, best practice for APIs)
# -------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change in production to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# Include Routers
# -------------------------
app.include_router(users.router)

# -------------------------
# Root endpoint
# -------------------------
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Hello, World!"}

# -------------------------
# Startup event
# -------------------------
@app.on_event("startup")
def on_startup():
    """
    Run startup tasks:
    - Create database tables (only for development, use Alembic in production)
    """
    Base.metadata.create_all(bind=engine)
    if settings.DEBUG:
        print("Database tables created and app started successfully.")
