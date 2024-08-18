import sqlite3

con = sqlite3.connect('test.db')

cur = con.cursor()

cur.execute("""CREATE TABLE label_info(
                label_id INTEGER,
                origin_image_path TEXT,
                save_image_path TEXT, 
                html TEXT
            )""")

con.commit()
con.close()