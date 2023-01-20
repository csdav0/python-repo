#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests
import random
import html
import os

URL="https://opentdb.com/api.php?amount=10&category=9&difficulty=medium&type=multiple" 

#picks a random question from API GET request
def questiongetter():
    rand = random.randint(0,9)
    data= requests.get(URL).json()
    questionpicker= data['results'][rand]
    return questionpicker


def make_question():
    #game logic below
    gen_question= questiongetter()
    answers= {}
    rand = random.randint(0,3)
    if rand == 0:
        answers['A']= gen_question['correct_answer']
        answers['B']= gen_question['incorrect_answers'][0]
        answers['C']= gen_question['incorrect_answers'][1]
        answers['D']= gen_question['incorrect_answers'][2]
        correctanswer= 'A'
    elif rand == 1:
        answers['A']= gen_question['incorrect_answers'][0]
        answers['B']= gen_question['correct_answer']
        answers['C']= gen_question['incorrect_answers'][1]
        answers['D']= gen_question['incorrect_answers'][2]
        correctanswer= 'B'
    elif rand == 2:
        answers['A']= gen_question['incorrect_answers'][0]
        answers['B']= gen_question['incorrect_answers'][1]
        answers['C']= gen_question['correct_answer']
        answers['D']= gen_question['incorrect_answers'][2]
        correctanswer= 'C'
    elif rand == 3:
        answers['A']= gen_question['incorrect_answers'][0]
        answers['B']= gen_question['incorrect_answers'][1]
        answers['C']= gen_question['incorrect_answers'][2]
        answers['D']= gen_question['correct_answer']
        correctanswer= 'D'        

    question= str(gen_question['question'])
    question= html.unescape(question)
    answerslist= html.unescape(answers)
    answer1= f"A: {answerslist['A']}"
    answer1= html.unescape(answer1)
    answer2= f"B: {answerslist['B']}"
    answer2= html.unescape(answer2)
    answer3= f"C: {answerslist['C']}"
    answer3= html.unescape(answer3)
    answer4= f"D: {answerslist['D']}"
    answer4= html.unescape(answer4)

    return question, answer1, answer2, answer3, answer4, correctanswer
