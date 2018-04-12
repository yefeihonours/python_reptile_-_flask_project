#coding:utf-8
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_bootstrap import Bootstrap

from flask_wtf import Form 
from wtforms import StringField, SubmitField 
from wtforms.validators import Required 
 
class NameForm(Form): 
    name = StringField('What is your name?', validators=[Required()]) 
    submit = SubmitField('提交')

app=Flask(__name__)
bootstrap=Bootstrap(app)
app.config['SECRET_KEY'] = 'hard to guess string'

@app.route('/', methods=['GET', 'POST']) 
def index(): 
    form = NameForm() 
    if form.validate_on_submit(): 
        old_name = session.get('name') 
        if old_name is not None and old_name != form.name.data: 
            flash('Looks like you have changed your name!') 
        session['name'] = form.name.data 
        return redirect(url_for('index')) 
    return render_template('index.html', form = form, name = session.get('name'))

#变量保存在用户会话中，即 session['name']，所以在两次请求之间也能记住输入的值

@app.errorhandler(404)  
def page_not_found(e):  
    return render_template('404.html'), 404  

if __name__=="__main__":
    app.run(debug=True)