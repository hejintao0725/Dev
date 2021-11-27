from flask import Blueprint, render_template, request, redirect, url_for, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import or_, and_, not_
from apps.user.models import *
from exts import db


user_bp1 = Blueprint('user', __name__)


# 首页
@user_bp1.route('/')
def index():
    # 1。cookie获取方式
    # uid = request.cookies.get('uid', None)
    # 2。session的获取,session底层默认获取
    # uid = session.get('uid')
    # if uid:
    #     user = User.query.get(uid)
    return render_template('user/register.html')
    # else:
    #     return render_template('user/index.html')


# 用户注册
@user_bp1.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')
        email = request.form.get('email')
        if password == repassword:
            # 注册用户
            user = User()
            user.username = username
            # 使用自带的函数实现加密：generate_password_hash
            user.password = generate_password_hash(password)
            user.phone = phone
            user.email = email
            # 添加并提交
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('user.login'))
    return render_template('user/register.html')



# 用户登录
@user_bp1.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        users = User.query.filter(User.username == username).all()
        for user in users:
            # 如果flag=True表示匹配，否则密码不匹配  user.password:数据库中的  password：表单提交的
            flag = check_password_hash(user.password, password)
            if flag:
                messages = Message.query.filter().all()  # 类似于select * from user;
                print(messages)
                return render_template('user/message_manage.html', messages=messages)

        else:
            return render_template('user/login.html', msg='用户名或者密码有误！')
    return render_template('user/login.html')




@user_bp1.route('/home')
def home():
    messages = Message.query.filter().all()
    return render_template('user/message_manage.html', messages=messages)


@user_bp1.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        stu_card = request.form.get('stu_card')  # 获取从前端传过来的学号
        if not stu_card:  # 判断学号不能为空
            return render_template('user/message_manage.html', msg='学号不能为空！')
        stu_name = request.form.get('stu_name')  # 获取从前端传过来的姓名
        if not stu_name:  # 判断姓名不能为空
            return render_template('user/message_manage.html', msg='姓名不能为空！')
        college = request.form.get('college')  # 获取从前端传过来的学院
        if not college:  # 判断学院不能为空
            return render_template('user/message_manage.html', msg='学院不能为空！')
        major = request.form.get('major')  # 获取从前端传过来的专业
        if not major:  # 判断专业不能为空
            return render_template('user/message_manage.html', msg='专业不能为空！')
        t_lass = request.form.get('t_lass')  # 获取从前端传过来的班级
        if not t_lass:  # 判断班级不能为空
            return render_template('user/message_manage.html', msg='班级不能为空！')
        course = request.form.get('course')  # 获取从前端传过来的课程
        if not course:  # 判断班级不能为空
            return render_template('user/message_manage.html', msg='课程不能为空！')
        score = request.form.get('score')  # 获取从前端传过来的分数
        if not score:  # 判断成绩不能为空
            return render_template('user/message_manage.html', msg='分数不能为空！')
        message = Message()
        message.stu_card = stu_card
        message.stu_name = stu_name
        message.college = college
        message.major = major
        message.t_lass = t_lass
        message.course = course
        message.score = score
        db.session.add(message)
        db.session.commit()
        # 查询数据库中的数据
        messages = Message.query.filter().all()  # 类似于select * from user;
        print(messages)  # [user_objA, user_objB,...]
        return render_template('user/message_manage.html', messages=messages, msg='新增数据成功！')
    return render_template('user/message_manage.html')


@user_bp1.route('/delete')
def delete():
     stu_card = request.args.get('id')
     print(stu_card)
     # 2.物理删除
     message = Message.query.get(stu_card)
     # 将对象放到缓存准备删除
     db.session.delete(message)
     # 提交删除
     db.session.commit()
     messages = Message.query.filter().all()  # 类似于select * from user;
     return render_template('user/message_manage.html', messages=messages)
     # return render_template('user/message_manage.html', )


@user_bp1.route('/modify', methods=['GET', 'POST'])
def modify():
    if request.method == 'POST':
        stu_card = request.form.get('stu_card')
        stu_name = request.form.get('stu_name')
        college = request.form.get('college')
        major = request.form.get('major')
        t_lass = request.form.get('t_lass')
        course = request.form.get('course')
        score = request.form.get('score')
        message = Message.query.get(stu_card)
        message.stu_card = stu_card
        message.stu_name = stu_name
        message.college = college
        message.major = major
        message.t_lass = t_lass
        message.course = course
        message.score = score
        db.session.commit()
        messages = Message.query.filter().all()  # 类似于select * from user;
        return render_template('user/message_manage.html', messages=messages)
    else:
        # 注意：前后端的id传值要保持一致
        stu_card = request.args.get('id')
        print(stu_card)
        message = Message.query.get(stu_card)
        return render_template('user/modify.html', message=message)

