from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_menu():
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/ask_questions')
def ask_question():
    return render_template('ask_questions.html')


@app.route('/answer_questions')
def answer_questions():
    return render_template('answer_questions.html')


@app.route('/user_setup')
def user_setup():
    return render_template('users.html')


@app.route('/log_out')
def log_out():
    return render_template('logout.html')


if __name__ == '__main__':
    app.run()
