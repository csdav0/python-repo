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


def main():
    #game instructions blurb
    while True:
        os.system("clear")
        user_input= input("\n\nTo exit the game at any time, answer 'stop'.\n\nIf you are ready to begin, press 'Enter'")
        if user_input == "":
            os.system("clear")
            break
    #game logic below
    user_score = 0
    question_count = 1
    while True:
        print(f"Question #{question_count}:")
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
        print(question)
        answerslist= str(answers)
        answerslist= html.unescape(answerslist)
        print(answerslist)
        useranswer= input("Make a selection:\n")
        if useranswer is correctanswer:
            print("Correct!\n")
            user_score += 1
            print(f"You've answered {user_score} / {question_count} questions correctly!\n")
            question_count += 1
        elif useranswer.lower() == "stop":
            break
        else:
            print("Sorry, that's incorrect!\n")
            question_count += 1

if __name__ == "__main__":
    main()

