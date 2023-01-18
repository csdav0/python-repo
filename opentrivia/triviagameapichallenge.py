#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests
import random
import html

URL="https://opentdb.com/api.php?amount=10&category=9&difficulty=medium&type=multiple" 

def questiongetter():
    rand = random.randint(0,9)
    data= requests.get(URL).json()
    questionpicker= data['results'][rand]
    return questionpicker


def main():

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

    #print(str(gen_question['question']))
    question= str(gen_question['question'])
    question= html.unescape(question)
    print(question)
    #print(str(answers))
    answerslist= str(answers)
    answerslist= html.unescape(answerslist)
    print(answerslist)
    useranswer= input("Make a selection:\n")
    if useranswer is correctanswer:
        print("Correct!")
    else:
        print("Sorry, that's incorrect!")

if __name__ == "__main__":
    main()

