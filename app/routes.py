from flask import render_template, request, redirect, url_for, flash, make_response
from app.forms import LoginForm

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        if username == 'admin' and password == 'secret':
            flash('Вход выполнен успешно!', 'success')
            resp = make_response(redirect(url_for('profile')))
            return resp
        else:
            flash('Неверное имя пользователя или пароль', 'error')
    
    return render_template('login.html', form=form)