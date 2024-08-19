import os
import shutil

def unlock_db():
    shutil.copy('/data/aisvc_data/intern2024_2/NLP_paper/label_data/label_info.db', '/data/aisvc_data/intern2024_2/NLP_paper/label_data/label_info_copy.db')
    os.rename('/data/aisvc_data/intern2024_2/NLP_paper/label_data/label_info.db', '/data/aisvc_data/intern2024_2/NLP_paper/label_data/label_info_locked.db')
    os.rename('/data/aisvc_data/intern2024_2/NLP_paper/label_data/label_info_copy.db', '/data/aisvc_data/intern2024_2/NLP_paper/label_data/label_info.db')
    # os.remove('/data/aisvc_data/intern2024_2/NLP_paper/label_data/label_info.db-journal')