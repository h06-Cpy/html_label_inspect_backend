from pydantic import BaseModel

class LabelInfoReq(BaseModel):
    label_id: int

    html: str

    struct_correct: int 
    char_correct: int 
    th_used: int 
    value_empty_cell: int 
    supsub: int 
    cell_subtitle: int 
    semantic_merged_cell: int 
    partial_lined: int