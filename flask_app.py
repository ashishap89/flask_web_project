from flask import Flask,render_template,url_for
app = Flask(__name__)

posts = [
    {
        'author': 'P.L. Deshpande',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 19, 1989'
    },
    {
        'author': 'V.P. Kalee',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 20, 1989'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)

