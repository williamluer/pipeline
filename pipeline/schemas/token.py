from datetime import datetime
from typing import Optional

from pydantic import validator

from .base import BaseModel, Patchable


class TokenGet(BaseModel):
    """API token representation when returned from an API call."""

    id: str
    #: Token value, used when authenticating with the API
    value: str
    #: Token value, used when authenticating with the API
    name: str
    #: Timestamp value of creation
    created_at: datetime
    #: Timestamp value of last update
    updated_at: datetime
    #: Timestamp value of expiry
    expires_at: Optional[datetime]
    #: Timestamp value of last usage
    last_used: Optional[datetime]
    #: If token is active (set by user and it's before its expiry date)
    is_active: bool
    #: Arbitrarily set user flag for token validity
    is_enabled: bool
    #: User associated with this token (if user token)
    user_id: Optional[str]


class TokenCreate(BaseModel):
    """Model for creating token"""

    #: Arbitrary name to be assigned to token
    name: Optional[str]
    #: Role name which assigns permissions
    type: str
    #: Timestamp value of future expiry
    expires_at: Optional[datetime]


class TokenPatch(Patchable):
    """Model for patching token"""

    # Arbitrary name to be assigned to token
    name: Optional[str]
    # Boolean specifying if token can be used
    is_enabled: Optional[bool]
    # Token value (only sudo tokens can use this)
    value: Optional[str]
    # Datetime to expire the token
    expire_at: Optional[datetime]

    @validator("is_enabled")
    def prevent_none(cls, v):
        if v is None:
            raise ValueError("must not be null")
        return v
