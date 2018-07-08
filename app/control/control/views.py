from . import control
from .services import *
from os import path
from .forms import LoginForm,AddForm,AddOtherForm
from flask import render_template,redirect,request,url_for
@control.route('/',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.username.data=='dp':
            return redirect('/index/update/QA')
        else:
            return '你输错了'
    return render_template('login.html',form=form)
@control.route('/update/<name>',methods=['GET','POST'])
def update(name):
    if name=='QA':
        form=AddForm()
        if request.method=='POST':
            if form.validate_on_submit():
                tag_num=form.type.data
                question=form.question.data
                answer=form.answer.data
                add(name,question,answer,tag_num)
                #把数据加入数据库
            return render_template('xx.html')
        else:
            return render_template('addsomething.html', form=form,name=name)
    elif name=='other':
            form=None
            form=AddOtherForm()
            if request.method=='POST':
                if form.validate_on_submit():
                    picture=request.files['picture']
                    file_name=upload(picture)
                    title=form.title.data
                    content=form.content.data
                    tag_num = form.type.data
                    add(name,file_name=file_name,title=title,content=content,tag_num=tag_num)
                return render_template('xx.html')
            else:
                return render_template('addsomething.html', form=form,name=name)
@control.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
@control.route('/login/',methods=['POST'])
def lo():
        APPID = 'wxe9f8ea2b5c9b1f26'
        SECRET = 'bd9151ef9d8d4baeed692e67cec9b16b'
        # 获取appid和secret
        data = request.get_data()
	print(data)
        # 拿到微信小程序发送code信息
        data_json = json.loads(data)
        JSCODE = data_json["code"]
        url = 'https://api.weixin.qq.com/sns/jscode2session?appid=' + APPID + '&secret=' + SECRET + '&js_code=' + JSCODE + '&grant_type=authorization_code'
        # 腾讯的ap
        print(url)
        res = requests.get(url).text
        resu_json = json.loads(res)
        if 'openid' in resu_json.keys():
            openid = resu_json["openid"]
            con = None
            cur = None
            try:
                con = get_connection()
                cur = con.cursor()
                sql = 'insert into `user` (id) VALUES (%s)'
                cur.execute(sql, openid)
                con.commit()
                session_key = resu_json["session_key"]
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
