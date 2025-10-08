from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError, jwt
from jwt import PyJWKClient

from modeling_you.configs import key_cloak
from modeling_you.types import Payload

# fetch the public key
jwk_client = PyJWKClient(key_cloak.JWK_URL)


def get_public_key(token: str):
    try:
        signing_key = jwk_client.get_signing_key_from_jwt(token)
        return signing_key.key
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))


security = HTTPBearer()


def verify_token(
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> Payload:
    token = credentials.credentials

    try:
        public_key = get_public_key(token)
        payload: Payload = jwt.decode(
            token,
            public_key,
            algorithms=[key_cloak.ALGORITHM],
            audience=key_cloak.AUDIENCE,
            issuer=f"{key_cloak.URL}",
        )
        return payload
    except JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )
