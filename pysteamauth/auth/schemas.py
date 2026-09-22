from typing import List, Optional

from pydantic import BaseModel


class Params(BaseModel):
    nonce: str
    auth: str


class TransferInfoItem(BaseModel):
    url: str
    params: Params


class FinalizeLoginStatus(BaseModel):
    steamID: Optional[str] = None
    redir: Optional[str] = None
    transfer_info: Optional[List[TransferInfoItem]] = None
    primary_domain: Optional[str] = None
