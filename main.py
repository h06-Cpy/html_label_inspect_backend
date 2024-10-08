from fastapi import FastAPI
from models import LabelInfoReq
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from save_label_info import save_html_image, save_db
from get_label_infos import get_one_label_info

app = FastAPI()

# 개발용 cors
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
      
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

# 개발용
app.mount('/assets', StaticFiles(directory="frontend/dist/assets"))

# 배포용
# app.mount('/assets', StaticFiles(directory="/code/frontend/dist/assets"))

@app.post("/save_label")
async def save_label(label_info: LabelInfoReq):
    try:
        origin_image_path, saved_image_path = save_html_image(label_info.originId, label_info.html, label_info.savedImage)

        save_db(label_info.originId, origin_image_path, saved_image_path, label_info.html)
        
    except Exception as e:
        print(e)
        raise(e)
        # return {"success": False, "message": str(e)}
    
    return {"success": True, "message": "label has been saved!"}


@app.get('/label_info/{label_id}')
async def get_label_info(label_id: int):

    return get_one_label_info(label_id)

@app.get("/")
async def index():
    return FileResponse("frontend/dist/index.html")