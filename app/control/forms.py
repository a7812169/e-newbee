from flask.ext.wtf import FlaskForm as Form
from wtforms import FileField,TextAreaField, SelectField,StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired
class LoginForm(Form):
    username = StringField(label=u'用户名',validators=[DataRequired()])
    password = PasswordField(label=u'密码',validators=[DataRequired()])
    submit = SubmitField(label=u'提交')
class AddForm(Form):
    question = StringField(label=u'问题', validators=[DataRequired()])
    answer = TextAreaField(label=u'回答', validators=[DataRequired()])
    type=SelectField('按类型添加',validators=[DataRequired()],choices=[('4','生活'),('5','缴费'),('6','交通'),('7','安全'),('8','住宿'),('9','报名'),('10','食堂')])
    submit = SubmitField(label=u'提交')
class AddOtherForm(Form):
    title = StringField(label=u'标题', validators=[DataRequired()])
    content = TextAreaField(label=u'内容', validators=[DataRequired()])
    type=SelectField('按类型添加',validators=[DataRequired()],choices=[('0','校园附近'),('1','武汉美食'),('2','游玩推荐'),('3','风景地区')])
    picture=FileField('照片',validators=[DataRequired()])
    submit = SubmitField(label=u'提交')
