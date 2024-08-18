import os
import json
import sqlite3
import base64

def get_one_label_info(origin_id):

    # json label 탐색

    # 개발용
    with open(f"test/json/{origin_id}.json", 'r') as fp:
        json_label = json.load(fp)

    # 배포용
    # with open(f"/data/aisvc_data/intern2024_2/NLP_paper/label_data/json/{label_id}.json", 'r') as fp:
    #     json_label = json.load(fp)


    html = json_label['html']
    # origin_image_path = json_label['origin_image_path']

    # assert(os.path.exists(origin_image_path) == True)

    # # 원본 이미지 base64 인코딩
    # with open(origin_image_path, 'rb') as fp:
    #     origin_image = base64.b64encode(fp.read())
    

    # db 조회
    
    # 개발용
    con = sqlite3.connect('test.db')
    
    # 배포용
    # con = sqlite3.connect('/data/aisvc_data/intern2024_2/NLP_paper/label_data/label_info.db')

    cur = con.cursor()

    res = cur.execute(f"SELECT COUNT(*) FROM label_info").fetchone()
    print(res)
    isInspected = False

    # 개발용 경로
    for name in os.listdir('test/saved_img'):
        if f'{origin_id}_' in name:
            isInspected = True
            break

    response = {
        "isInspected": isInspected,
        "originHtml": html,
        "totalGeneratedNum": res[0]
    }
   
    
    con.close()

    return response
    

