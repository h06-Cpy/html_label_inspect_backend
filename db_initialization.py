import sqlite3

con = sqlite3.connect('test.db')

cur = con.cursor()

cur.execute("""CREATE TABLE label_info(
                label_id INTEGER PRIMARY KEY,
                origin_image_path TEXT,
                struct_correct INTEGER, 
                char_correct INTEGER, 
                th_used INTEGER, 
                value_empty_cell INTEGER, 
                special_char Text, 
                cell_subtitle Text, 
                semantic_merged_cell Text, 
                partial_lined Text,
                topleft_header Text
            )""")

con.commit()
con.close()