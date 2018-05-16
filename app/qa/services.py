from .. import get_connection
from  flask import request
def get(tag):
    conn=get_connection()
    cur=conn.cursor()
    sql='select question,answer,id from qa where tag_id=%s'
    cur.execute(sql,tag)
    res=cur.fetchall()
    data=[]
    for i in res:
        list={
        "question":i[0],
        "answer":i[1],"id":i[2]}
        data.append(list)
    cur.close()
    conn.close()
    return data
def get_seach():
    if request.method=='POST':
        questison=request.form['question']
        conn=get_connection()
        cur=conn.cursor()
        arg='%'+questison+'%'
        sql='select id,question,answer from qa WHERE question like %s'
        cur.execute(sql,arg)
        res=cur.fetchall()
        data=[]
        for i in res:
            list={
                "id":i[0],"question":i[1],"answer":i[2]}
            data.append(list)
        return data
    else:
        return None