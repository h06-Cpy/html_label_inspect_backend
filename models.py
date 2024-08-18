from pydantic import BaseModel
from typing import List

class LabelInfoReq(BaseModel):
    originId: int
    savedImage: str
    html: str