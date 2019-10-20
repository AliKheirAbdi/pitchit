from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '204d90519db10b4c'

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


@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = RegistrationForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
