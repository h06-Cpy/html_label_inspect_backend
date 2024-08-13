from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from save_label_info import save_html, save_db
from models import LabelInfoReq

app = FastAPI()

origins = [
    'http://localhost:5172',
    'https://localhost:5172',
    'http://127.0.0.1:5172',
    'https://127.0.0.1:5172',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/save_label")
async def save_label(label_info: LabelInfoReq):
    try:
        origin_image_path = save_html(label_info.label_id, label_info.html)

        save_db(origin_image_path,
        label_info.struct_correct,
        label_info.char_correct,
        label_info.th_used,
        label_info.value_empty_cell,
        label_info.supsub,
        label_info.cell_subtitle,
        label_info.semantic_merged_cell,
        label_info.partial_lined)
        
    except Exception as e:
        print(e)
        return {"success": False, "message": str(e)}
    
    return {"success": True, "message": "label has been saved!"}


@app.get('/label_info/{label_id}')
async def get_label_info(label_id: int):
    # db 조회

    # 검수 안된 경우

    # 검수 한 경우
    pass

@app.get("/")
async def root():
    return {"message": "Hello World"}