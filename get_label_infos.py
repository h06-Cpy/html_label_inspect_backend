import os
import json
import sqlite3
import base64

def _get_label_info(label_id):
    # json label 탐색
    with open(f"test/json/{label_id}.json", 'r') as fp:
        json_label = json.load(fp)

    html = json_label['html']
    origin_image_path = json_label['origin_image_path']

    assert(os.path.exists(origin_image_path) == True)

    # 원본 이미지 base64 인코딩
    with open(origin_image_path, 'rb') as fp:
        origin_image = base64.b64encode(fp.read())
    

    # db 조회
    con = sqlite3.connect('test.db')
    cur = con.cursor()

    res = cur.execute(f"SELECT * FROM label_info WHERE label_id={label_id}").fetchone()

    # 검수 안된 경우
    if res is None:
        response = {
            "inspected": False,
            "html": html,
            "imageName": origin_image_path.split('.')[-1],
            "originImage": origin_image
        }
    
    # 검수 한 경우
    else:
        (_, _, struct_correct, char_correct, th_used, value_empty_cell, supsub, cell_subtitle, semantic_merged_cell, partial_lined) = res
        
        response = {
            "inspected": True,
            "html": html,
            "imageName": origin_image_path.split('/')[-1],
            "originImage": origin_image,
            "structCorrect": bool(struct_correct),
            "charCorrect": bool(char_correct),
            "thUsed": bool(th_used),
            "valueEmptyCell": bool(value_empty_cell),
            "supsub": supsub,
            "cellSubtitle": cell_subtitle,
            "semanticMergedCell": semantic_merged_cell,
            "partialLined": partial_lined
        }
    
    con.close()

    return response
    

# 집계 정보 반환
def _get_agg_info():
    pass