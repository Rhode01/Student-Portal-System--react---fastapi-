from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.router import api_router
app = FastAPI(title="Student Portal API")

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
