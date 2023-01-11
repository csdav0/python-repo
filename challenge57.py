#!/usr/bin/env python3
import html

trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }

correctslice = trivia["correct_answer"]
correctanswer = html.unescape(correctslice)
incorrectslice1 = trivia["incorrect_answers"][0]
incorrectanswer1 = html.unescape(incorrectslice1)
incorrectslice2 = trivia["incorrect_answers"][1]
incorrectanswer2 = html.unescape(incorrectslice2)
incorrectslice3 = trivia["incorrect_answers"][2]
incorrectanswer3 = html.unescape(incorrectslice3)

print("Prepare for a movie trivia question!")
print(trivia["question"])
print("Is it (A): ", correctanswer)
print("Is it (B): ", incorrectanswer1)
print("Is it (C): ", incorrectanswer2)
print("Is it (D): ", incorrectanswer3)

round = 0
while True:
    useranswer= input("Please make your selection:\n")
    
    if useranswer.isdigit():
        print("You must choose A, B, C, or D!")
    elif len(useranswer) != 1:
        print("You must choose A, B, C, or D!")
    elif useranswer.isalnum() != True:
        print("You must choose A, B, C, or D!")
    elif useranswer.capitalize() == "A" or useranswer.capitalize() == "B" or useranswer.capitalize() == "C" or useranswer.capitalize() == "D":
        if useranswer.capitalize() == "A":
            print("Correct!")
            break
        else:
            print("Sorry, that's incorrect!")
            break
    else:
        print("You must choose A, B, C, or D!")
