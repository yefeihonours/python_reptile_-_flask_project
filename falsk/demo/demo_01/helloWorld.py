from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'Hello %s!' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

if __name__ == '__main__':
    app.run(debug='True')