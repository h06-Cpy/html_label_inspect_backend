import json
import sqlite3
import base64
import os
from db_unlock import unlock_db

root_path = 'test'

def save_html_image(origin_id:int, html: str, saved_image: str):
    
    # 개발용
    with open(f"{root_path}/json/{origin_id}.json", 'r') as fp:
        json_label = json.load(fp)
        json_label['html'] = html
        origin_image_path = json_label['origin_image_path']
    
    with open(f"{root_path}/json/{origin_id}.json", 'w') as fp:
        json.dump(json_label, fp)

    id_to_save = 0
    for name in os.listdir(f'{root_path}/saved_img'):
        if f"{origin_id}_{id_to_save}.png" == name:
            id_to_save += 1

    # 개발용 이미지 저장 경로
    saved_image_path = f"{root_path}/saved_img/{origin_id}_{id_to_save}.png"

    with open(saved_image_path, 'wb') as fp:
        fp.write(base64.b64decode(saved_image.replace('data:image/png;base64,','')))

    return origin_image_path, saved_image_path

    
    # 배포용
    # with open(f"/data/aisvc_data/intern2024_2/NLP_paper/label_data/json/{label_id}.json", 'r') as fp:

    #     json_label = json.load(fp)
    #     json_label['html'] = html
    #     origin_image_path = json_label['origin_image_path']
    
    # with open(f"/data/aisvc_data/intern2024_2/NLP_paper/label_data/json/{label_id}.json", 'w') as fp:
    #     json.dump(json_label, fp)

    # return origin_image_path

def save_db(origin_id:int, origin_image_path: str, saved_image_path:str, html: str):
    def _save_db(origin_id:int, origin_image_path: str, saved_image_path:str, html: str):

        # 개발용 db
        con = sqlite3.connect('test.db')
        
        # 배포용
        # con = sqlite3.connect('/data/aisvc_data/intern2024_2/NLP_paper/label_data/label_info.db')
        
        cur = con.cursor()
        cur.execute('PRAGMA journal_mode=WAL;')
        con.commit()

        res = cur.execute(f"SELECT * FROM label_info WHERE save_image_path='{saved_image_path}'")

        if res.fetchone() is None:
            print('insert!')

            cur.execute('INSERT INTO label_info (origin_id, origin_image_path, save_image_path, html) VALUES (?, ?, ?, ?)', (origin_id, origin_image_path, saved_image_path, html))

        else:
            print('update!')

            cur.execute(f"""UPDATE label_info SET html={html} WHERE save_image_path='{saved_image_path}'""")

        con.commit()
        con.close()
    


    try: 
        _save_db(origin_id, origin_image_path, saved_image_path, html)
    
    except sqlite3.OperationalError:
        print('db locked!')

        unlock_db()

        _save_db(origin_id, origin_image_path, saved_image_path, html)