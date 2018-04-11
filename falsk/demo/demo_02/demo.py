from flask import Flask, make_response, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/cookie') 
def cookies(): 
    response = make_response('<h1>This document carries a cookie!</h1>') 
    response.set_cookie('answer', '43')
    return response

@app.route('/') 
def index(): 
    return redirect(url_for('greet', name='Flask'))

@app.route('/greet')
def greet2():
    name = request.args['name']
    return render_template('user.html', name=name)

@app.route('/user/<name>')
def greet(name):
    return render_template('user.html',name=name)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)