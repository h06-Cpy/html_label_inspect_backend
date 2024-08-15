import os
import json
import sqlite3
import base64

def get_one_label_info(label_id):

    # json label 탐색

    # 개발용
    with open(f"test/json/{label_id}.json", 'r') as fp:
        json_label = json.load(fp)

    # 배포용
    # with open(f"/data/aisvc_data/intern2024_2/NLP_paper/label_data/json/{label_id}.json", 'r') as fp:
    #     json_label = json.load(fp)


    html = json_label['html']
    origin_image_path = json_label['origin_image_path']

    assert(os.path.exists(origin_image_path) == True)

    # 원본 이미지 base64 인코딩
    with open(origin_image_path, 'rb') as fp:
        origin_image = base64.b64encode(fp.read())
    

    # db 조회
    
    # 개발용
    con = sqlite3.connect('test.db')
    
    # 배포용
    # con = sqlite3.connect('/data/aisvc_data/intern2024_2/NLP_paper/label_data/label_info.db')

    cur = con.cursor()

    res = cur.execute(f"SELECT * FROM label_info WHERE label_id={label_id}").fetchone()

    # 검수 안된 경우
    if res is None:
        response = {
            "inspected": False,
            "html": html,
            "imageName": origin_image_path.split('/')[-1],
            "originImage": origin_image
        }
    
    # 검수 한 경우
    else:
        (_, _, struct_correct, char_correct, th_used, value_empty_cell, special_char, cell_subtitle, semantic_merged_cell, partial_lined, topleft_header) = res
        
        response = {
            "inspected": True,
            "html": html,
            "imageName": origin_image_path.split('/')[-1],
            "originImage": origin_image,
            "structCorrect": bool(struct_correct),
            "charCorrect": bool(char_correct),
            "thUsed": bool(th_used),
            "valueEmptyCell": bool(value_empty_cell),
            "specialChar": [int(i) for i in special_char.split()],
            "cellSubtitle": [int(i) for i in cell_subtitle.split()],
            "semanticMergedCell": [int(i) for i in semantic_merged_cell.split()],
            "partialLined": [int(i) for i in partial_lined.split()],
            "topleftHeader": [int(i) for i in topleft_header.split()]
        }
    
    con.close()

    return response
    

# 집계 정보 반환
def _get_agg_info():
    pass