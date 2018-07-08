from app import get_connection
from flask import request
import json
from flask import jsonify
import requests
import redis
import uuid
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
    file_name = "/home/image/"+picture.filename
    picture.save(file_name)
    url_address="https://qunawang.top/image/"+picture.filename
    return url_address
def login2():
    APPID = 'wxe9f8ea2b5c9b1f26'
    SECRET = 'bd9151ef9d8d4baeed692e67cec9b16b'
    # 获取appid和secret
    data = request.get_json()
    # 拿到微信小程序发送code信息
    JSCODE = data["code"]
    url = 'https://api.weixin.qq.com/sns/jscode2session?appid=' + APPID + '&secret=' + SECRET + '&js_code=' + JSCODE + '&grant_type=authorization_code'
    # 腾讯的ap
    print(url)
    res = requests.get(url).json()
    print(type(res))
    if 'openid' in res.keys():
        openid = res["openid"]
        con = None
        cur = None
        try:
            con = get_connection()
            cur = con.cursor()
            sql = 'INSERT INTO `user` (id) VALUES (%s)'
            cur.execute(sql, openid)
            con.commit()
            session_key = res["session_key"]
            # 访问腾讯给的接口用code换取openid和session——
            sessionid = uuid.uuid1()
            # 随机生产sessionid作为key
            value = '"openid":"{}","session_key":"{}"'.format(openid, session_key)
            # openid和session_key作为value
            conn = redis.StrictRedis(host='120.79.154.232', port=6379)
            # 连接redis数据库ps这里我是试用我自己的来测试
            conn.hset("3rd_sessionid", sessionid, value)
            # 数据传入数据库
            return jsonify({'code': 1, 'msg': '获取成功', 'data': sessionid})
        except Exception as e:
            con.rollback()
            raise e
        finally:
            if con is not None:
                cur.close()
                con.close()
    else:
        return jsonify({'code': 0, 'msg': '获取失败', 'data': None})
def get(tag):
    conn=get_connection()
    cur=conn.cursor()
    sql='select url,content,title from for_something where tag_id=%s'
    cur.execute(sql,tag)
    res=cur.fetchall()
    data=[]
    for i in res:
        list={
        "url":i[0],
        "content":i[1],"title":i[2]}
        data.append(list)
    cur.close()
    conn.close()
    return data