#!/usr/bin/env python3

wordbank = ["indentation","spaces"]
tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']
wordbank.append(4)
print(wordbank)

num = input("Enter a number between 0 and 20 inclusive: ")
num = int(num)
student_name = tlgstudents[num]
print(student_name + " always uses " + wordbank[2].__str__() + " " +  wordbank[1] + " to indent.")

