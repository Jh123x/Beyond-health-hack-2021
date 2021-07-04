from flask import Flask
from flask.templating import render_template

app = Flask(__name__)

class Blog(object):
    def __init__(self):
        self.title = "title"
        self.comments = [("comment1", 'author1'), ("comment2", 'author2')]
        self.body = "body"
        self.likes = 3

blog = Blog()


@app.route('/')
def index():
    return render_template('main.html', blog = blog)


@app.route('/test')
def test():
    return render_template('testpage.html', blog=blog)


if __name__ == "__main__":
    app.run(debug=True)