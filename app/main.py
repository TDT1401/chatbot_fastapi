from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from app.api.api_router import api_router, auth_router, chatbot_router
from app.core.config import get_settings

# Load environment variables from .env file
app = FastAPI(
    title="minimal fastapi postgres template",
    version="6.1.0",
    openapi_url="/openapi.json",
    docs_url="/",
)
load_dotenv()

app.include_router(auth_router)
app.include_router(api_router)
app.include_router(chatbot_router)

# Sets all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        str(origin).rstrip("/")
        for origin in get_settings().security.backend_cors_origins
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Guards against HTTP Host Header attacks
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=get_settings().security.allowed_hosts,
)
