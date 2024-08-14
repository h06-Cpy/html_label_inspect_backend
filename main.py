from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
from models import LabelInfoReq
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from save_label_info import save_html, save_db
from get_label_infos import _get_label_info

app = FastAPI()

# origins = [
#     'http://localhost:5173',
#     'https://localhost:5173',
#     'http://127.0.0.1:5173',
#     'https://127.0.0.1:5173',
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# 개발용
# app.mount('/assets', StaticFiles(directory="frontend/dist/assets"))

# 배포용
app.mount('/assets', StaticFiles(directory="/code/frontend/dist/assets"))

@app.post("/save_label")
async def save_label(label_info: LabelInfoReq):
    try:
        origin_image_path = save_html(label_info.label_id, label_info.html)

        save_db(label_info.label_id, origin_image_path,
        label_info.struct_correct,
        label_info.char_correct,
        label_info.th_used,
        label_info.value_empty_cell,
        label_info.supsub,
        label_info.cell_subtitle,
        label_info.semantic_merged_cell,
        label_info.partial_lined,
        label_info.topleft_header)
        
    except Exception as e:
        print(e)
        # raise(e)
        return {"success": False, "message": str(e)}
    
    return {"success": True, "message": "label has been saved!"}


@app.get('/label_info/{label_id}')
async def get_label_info(label_id: int):

    return _get_label_info(label_id)

@app.get("/")
async def index():
    return FileResponse("frontend/dist/index.html")