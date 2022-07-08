# -*-coding:utf-8-*-
# Autor:编程的小姐姐
# DateTime:2022/4/22 22:01
# File:03-flask-wtf
from flask import Flask, request, render_template, url_for,redirect,jsonify
# 导入wtf扩展的表单类
from flask_wtf import FlaskForm
# 导入自定义表单需要的字段
from wtforms import SubmitField, StringField, PasswordField, SelectMultipleField, RadioField
# 导入wtf扩展提供的表单验证器
from wtforms.validators import DataRequired, EqualTo, Length, Regexp


app = Flask(__name__)

app.config["SECRET_KEY"] = "2534d1aaggada3"

class MyForm(FlaskForm):
    username = StringField(label='用户名',
                           validators=[DataRequired(),Length(4,10)]
                           )

    password = PasswordField(label='密码',
                           validators=[DataRequired(),Regexp('[0-9a-zA-Z!@#$%^&*()]{6,16}')]
                           )

    check_password = PasswordField(label='确认密码',
                           validators=[DataRequired(),EqualTo("password","check_password")]
                           )

    # 下拉多选框
    select = SelectMultipleField(label='多选', choices=[('0', 'flask'),('1', 'python'),('2', 'django')],
                                 validators=[DataRequired()])
    # 单选框,这里特别注意 coerce参数指定元祖中第一个参数的数据类型，否则校验失败
    radio = RadioField(label="性别", choices=[(0, '女'), (1, '男')], coerce=int)
    # 提交表单
    submit = SubmitField(label='提交')


@app.route('/',methods=["get",'post'])
def register():
    form = MyForm()
    if request.method == "GET":
        return render_template('register.html',form=form)

    elif request.method == "POST":

        if form.validate_on_submit(): #如果验证通过
            dic = {}
            dic["username"] = form.username.data
            dic["password"] = form.password.data
            dic["check_password"] = form.check_password.data
            dic["select"] = form.select.data
            dic["radio"] = form.radio.data
            return jsonify(dic)
        else: #验证失败
            return render_template('register.html',form=form)




if __name__ == '__main__':
    app.run(debug=True)





