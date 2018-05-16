from .. import get_connection
from  flask import request
def get(tag):
    conn=get_connection()
    cur=conn.cursor()
    sql='select title,content,url_address from article where tag_id=%s'
    cur.execute(sql,tag)
    res=cur.fetchall()
    data=[]
    for i in res:
        list={
        "title":i[0],
        "url_address":i[1],
        "content":i[2],}
        data.append(list)
    cur.close()
    conn.close()
    return data
def get_seach():
    if request.method=='POST':
        title=request.form['title']
        conn=get_connection()
        cur=conn.cursor()
        arg='%'+title+'%'
        sql='select title,content,url_address from article WHERE title like %s'
        cur.execute(sql,arg)
        res=cur.fetchall()
        data=[]
        for i in res:
            list={
                "title":i[0],"content":i[1],"url_address":i[2]}
            data.append(list)
        return data
    else:
        return None