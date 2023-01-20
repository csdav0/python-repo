#!/usr/bin/python3
"""Alta3 Research
Simple flask application using redirect()"""

from flask import Flask
from flask import redirect
from flask import url_for
from flask import render_template
from flask import request
from flask import abort
from triviagameapichallenge2 import make_question

app = Flask(__name__)

pic_location= "https://images.unsplash.com/photo-1599508704512-2f19efd1e35f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1335&q=80"
pic2_location= "https://media4.giphy.com/media/Od0QRnzwRBYmDU3eEO/giphy.gif?cid=ecf05e47agh7nlz8sfsrt7njmhqzq51nw4mvo4hi1u0vfa6q&rid=giphy.gif&ct=g"

# if user sends GET to / (root)
@app.route("/")
def index():
    question_call = make_question()
    global correct_answer
    correct_answer = question_call[5]
    return render_template("questionV2.html", pic= pic_location, question= question_call[0], answer1= question_call[1], answer2= question_call[2], answer3= question_call[3], answer4= question_call[4])  
# found in templates/

# if user sends GET or POST to /login
@app.route("/login", methods = ["POST", "GET"])
def login():
    # if user sent a POST
    if request.method == "POST":
        # if the POST contains '42' as the value for 'answer'
        if request.form["answer"].upper() == correct_answer:
            return redirect(url_for("success")) # return a 302 redirect to /success
        else:
            return redirect(url_for("fail"))    # return a 302 redirect to /fail
    elif request.method == "GET":
        return redirect(url_for("index")) # if they sent a GET to /login send 302 redirect to /

@app.route("/httpfail")
def httpfail():
    abort(406)  # send back a HTTP failure

@app.route("/fail")
def fail():
    return render_template("fail.html")    

@app.route("/success")
def success():
    return render_template("correct.html", pic= pic2_location)

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)

