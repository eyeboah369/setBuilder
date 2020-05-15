from flask import render_template, redirect, url_for, flash, request
from app import app
from app.forms import LoginForm, AnswerForm

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', title='SetBuilder')

@app.route("/start", methods=['GET', 'POST'])
def start():
    form = LoginForm()
    if form.validate_on_submit():
        name = form.username.data
        print("Log of username:", name)
        #flash('Username set!, welcome {}'.format(name))
        return redirect(url_for('game', valid_name=name))
    return render_template('login.html', form=form)

@app.route("/game/<valid_name>")
@app.route("/game")
def game(valid_name):
    return render_template('game.html', username=valid_name)

@app.route("/level1", methods=['GET', 'POST'])
def level1():
    answerForm = AnswerForm()
    if answerForm.validate_on_submit():
        answer = answerForm.userAnswer.data
        print("This is the users submitted answer: ", answer)
        if answer == "|3|CC(B^A')":
            return redirect(url_for('game', valid_name=" "))
    return render_template('level1.html', answerForm=answerForm)

@app.route("/level2", methods=['GET', 'POST'])
def level2():
    answerForm = AnswerForm()
    if answerForm.validate_on_submit():
        answer = answerForm.userAnswer.data
        print("This is the users submitted answer: ", answer)
        if answer == "|F^M'|>|S^C|":
            return redirect(url_for('game', valid_name=" "))
    return render_template('level2.html', answerForm=answerForm)

@app.route("/level3", methods=['GET', 'POST'])
def level3():
    answerForm = AnswerForm()
    if answerForm.validate_on_submit():
        answer = answerForm.userAnswer.data
        print("This is the users submitted answer: ", answer)
        if answer == "|F^M'|>|S^C|":
            return redirect(url_for('game', valid_name=" "))
    return render_template('level3.html', answerForm=answerForm)
