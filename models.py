from pydantic import BaseModel

class LabelInfoReq(BaseModel):
    label_id: int

    html: str

    struct_correct: bool 
    char_correct: bool 
    th_used: bool 
    value_empty_cell: bool
    supsub: int 
    cell_subtitle: int 
    semantic_merged_cell: int 
    partial_lined: int
    topleft_header: int