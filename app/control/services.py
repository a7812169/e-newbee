from app import get_connection
from flask import request
from os import path
def add(name,question=None,answer=None,tag_num=None,title=None,content=None,file_name=None):
    conn=None
    cur=None
    if name=='other':
        conn=get_connection()
        cur=conn.cursor()
        sql='insert into article(title,url_address,content,tag_id)VALUES (%s,%s,%s,%s)'
        try:
            cur.execute(sql,(title,file_name,content,tag_num))
            conn.commit()
        finally:
            conn.close()
            cur.close()
    elif name=='QA':
        conn = get_connection()
        cur = conn.cursor()
        sql = 'insert into qa(question,answer,tag_id)VALUES (%s,%s,%s)'
        try:
            cur.execute(sql, (question, answer, tag_num))
            conn.commit()
        except Exception as e:
            conn.rollback()
        finally:
            conn.close()
            cur.close()
def upload(picture=None):
    base_path = path.abspath(path.dirname(__file__))
    upload_path = path.join(base_path, '')
    file_name = upload_path + picture.filename
    picture.save(file_name)
    return file_name