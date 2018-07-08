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
    return login2()

