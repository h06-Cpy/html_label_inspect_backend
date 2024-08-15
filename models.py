from pydantic import BaseModel
from typing import List

class LabelInfoReq(BaseModel):
    label_id: int

    html: str

    struct_correct: bool 
    char_correct: bool 
    th_used: bool 
    value_empty_cell: bool
    special_char: List[int]
    cell_subtitle: List[int] 
    semantic_merged_cell: List[int] 
    partial_lined: List[int]
    topleft_header: List[int]