from fastapi import Depends, HTTPException
from fastapi.security import OAuth2AuthorizationCodeBearer
from jose import jwt
from jose.exceptions import JWTError
from authlib.jose import JsonWebKey
from sqlalchemy.ext.asyncio import AsyncSession
import requests
from fastapi import APIRouter
from authlib.integrations.starlette_client import OAuth
from app.core.db.config import settings
oauth = OAuth()
oauth.register(
    name='OAuth',
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        'scope': 'openid profile email',
        'audience': settings.AUTH0_API_AUDIENCE
    },
    server_metadata_url=f'https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration'
)

router = APIRouter()
oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=f"https://{settings.AUTH0_DOMAIN}/authorize",
    tokenUrl=f"https://{settings.AUTH0_DOMAIN}/oauth/token"
)
