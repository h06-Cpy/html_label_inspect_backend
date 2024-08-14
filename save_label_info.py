import json
import sqlite3

def save_html(label_id:int, html: str):
    
    # 개발용
    # with open(f"test/json/{label_id}.json", 'r') as fp:
    
    # 배포용
    with open(f"/data/aisvc_data/intern2024_2/NLP_paper/label_data/json/{label_id}.json", 'r') as fp:

        json_label = json.load(fp)
        json_label['html'] = html
        origin_image_path = json_label['origin_image_path']
    
    with open(f"/data/aisvc_data/intern2024_2/NLP_paper/label_data/json/{label_id}.json", 'w') as fp:
        json.dump(json_label, fp)

    return origin_image_path

def save_db(label_id:int, origin_image_path: str,
    struct_correct: bool,
    char_correct: bool,
    th_used: bool,
    value_empty_cell: bool,
    supsub: int,
    cell_subtitle: int,
    semantic_merged_cell: int,
    partial_lined: int,
    topleft_header: int):

    
    # 개발용
    # con = sqlite3.connect('test.db')
    
    # 배포용
    con = sqlite3.connect('/data/aisvc_data/intern2024_2/NLP_paper/label_data/label_info.db')
    cur = con.cursor()

    res = cur.execute(f"SELECT * FROM label_info WHERE label_id={label_id}")
   
   # 검수 안된 레이블
    if res.fetchone() is None:
        print('insert!')
        cur.execute(f"""INSERT INTO label_info VALUES 
                   ({label_id}, '{origin_image_path}', {struct_correct}, {char_correct}, 
                   {th_used}, {value_empty_cell}, {supsub}, {cell_subtitle}, {semantic_merged_cell}, {partial_lined}, {topleft_header})""")
   
   # 검수된 레이블
    else:
        print('update!')

        cur.execute(f"""
            UPDATE label_info SET
                struct_correct={struct_correct},
                char_correct={char_correct},
                th_used={th_used},
                value_empty_cell={value_empty_cell},
                supsub={supsub},
                cell_subtitle={cell_subtitle},
                semantic_merged_cell={semantic_merged_cell},
                partial_lined={partial_lined},
                topleft_header={topleft_header}

            WHERE label_id={label_id}
        """)

    con.commit()
    con.close()