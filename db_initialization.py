import sqlite3

con = sqlite3.connect('test.db')

cur = con.cursor()

cur.execute("""CREATE TABLE label_info(
                origin_image_path TEXT,
                struct_correct INTEGER, 
                char_correct INTEGER, 
                th_used INTEGER, 
                value_empty_cell INTEGER, 
                supsub INTEGER, 
                cell_subtitle INTEGER, 
                semantic_merged_cell INTEGER, 
                partial_lined INTEGER 
            )""")


# cur.execute("""INSERT INTO label_info VALUES ('/hello', 0, 0, 0, 0, 0, 0, 0, 0)""")
# con.commit()

# res = cur.execute("SELECT * FROM label_info")
# assert(res.fetchone() == ('/hello', 0, 0, 0, 0, 0, 0, 0, 0))

# cur.execute("DELETE FROM label_info")


con.commit()
con.close()