from flask import render_template, redirect, url_for, flash, request
from app import app
from app.forms import LoginForm, AnswerForm

#index/home page landing page for apps launch
@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', title='SetBuilder')

#route for user to enter their name into the program
@app.route("/start", methods=['GET', 'POST'])
def start():
    form = LoginForm()
    if form.validate_on_submit():
        name = form.username.data
        print("Log of username:", name)
        #flash('Username set!, welcome {}'.format(name))
        return redirect(url_for('game', valid_name=name))
    return render_template('login.html', form=form)

#route for the user to see the levels of the setBuilder game they can play
@app.route("/game/<valid_name>")
@app.route("/game")
def game(valid_name):
    return render_template('game.html', username=valid_name)

#route for level 1
@app.route("/level1", methods=['GET', 'POST'])
def level1():
    answerForm = AnswerForm()
    if answerForm.validate_on_submit():
        answer = answerForm.userAnswer.data
        print("This is the users submitted answer: ", answer)
        if answer == "|3|CC(B^A')":
            return redirect(url_for('game', valid_name=" "))
    return render_template('level1.html', answerForm=answerForm)

#route for level 2
@app.route("/level2", methods=['GET', 'POST'])
def level2():
    answerForm = AnswerForm()
    if answerForm.validate_on_submit():
        answer = answerForm.userAnswer.data
        print("This is the users submitted answer: ", answer)
        if answer == "|F^M'|>|S^C|":
            return redirect(url_for('game', valid_name=" "))
    return render_template('level2.html', answerForm=answerForm)

#route for level 3
@app.route("/level3", methods=['GET', 'POST'])
def level3():
    answerForm = AnswerForm()
    if answerForm.validate_on_submit():
        answer = answerForm.userAnswer.data
        print("This is the users submitted answer: ", answer)
        if answer == "E^(HUU)'":
            return redirect(url_for('game', valid_name=" "))
    return render_template('level3.html', answerForm=answerForm)

#route for level 4
@app.route("/level4", methods=['GET', 'POST'])
def level4():
    answerForm = AnswerForm()
    if answerForm.validate_on_submit():
        answer = answerForm.userAnswer.data
        print("This is the users submitted answer: ", answer)
        if answer == "(CUR)CCP":
            return redirect(url_for('game', valid_name=" "))
    return render_template('level4.html', answerForm=answerForm)
