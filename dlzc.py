pip install flask
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///registration.db'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User(username=username, password=password)
        db.session.add(user)
        ***mit()
        flash('注册成功！')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('登录失败，请检查用户名或密码')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>注册登录示例</title>
    <link href="***/ajax/libs/bootstrap/5.1.0/css/bootstrap.min.css" rel="stylesheet">
    <script src="***/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <script src="***/ajax/libs/bootstrap/5.1.0/js/bootstrap.min.js"></script>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container">
            <a class="navbar-brand" href="#">注册登录示例</a>
            <ul class="navbar-nav">
                <li class="nav-item"><a class="nav-link" href="{{ url_for('register') }}">注册</a></li>
                <li class="nav-item"><a class="nav-link" href="{{ url_for('login') }}">登录</a></li>
                       </ul>
        </div>
    </nav>
    <div class="container mt-5">
        {% block content %}
        {% endblock %}
    </div>
</body>
</html>
{% extends 'base.html' %}

{% block content %}
<h1>注册</h1>
<form method="post" action="{{ url_for('register') }}">
    <div class="mb-3">
        <label for="username" class="form-label">用户名</label>
        <input type="text" class="form-control                   id="username" aria-describedby="usernameHelp">
    </div>
    <div class="mb-3">
        <label for="password" class="form-label">密码</label>
        <input type="password" class="form-control" id="password">
    </div>
    <button type="submit" class="btn btn-primary">注册</button>
</form>
{% endblock %}
{% extends 'base.html' %}

{% block content %}
<h1>登录</h1>
<form method="post" action="{{ url```
/login }}">
    <div class="mb-3">
        <label for="username" class="form-label">用户名</label>
        <input type="text" class="form-control" id="username">
    </div>
    <div class="mb-3">
        <label for="password" class="form-label">密码</label>
        <input type="password" class="form-control" id="password">
    </div>
    <button type="submit" class="btn btn-primary">登录</button>
</form>
{% endblock %}
