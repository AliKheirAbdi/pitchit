from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Jane Doe',
        'title': 'pitch 1',
        'content': 'first pitch',
        'date_posted': 'October 18, 2019',
    },
    {
        'author': 'Ali Kheir',
        'title': 'pitch 2',
        'content': 'second pitch',
        'date_posted': 'October 20, 2019'
    }

]


@app.route('/')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
