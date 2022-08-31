import random
q1 = """Who developed Python Programming Language?
a) Wick van Rossum
b) Rasmus Lerdorf
c) Guido van Rossum
d) Niene Stom"""
q2 = """Which type of Programming does Python support?
a) object-oriented programming
b) structured programming
c) functional programming
d) all of the mentioned"""
q3 = """Which of the following is the correct extension of the Python file?
a) .python
b) .pl
c) .py
d) .p"""
q4 = """Which of the following is used to define a block of code in Python language?
a) Indentation
b) Key
c) Brackets
d) All of the mentioned"""
q5 = """Which keyword is used for function in Python language?
a) Function
b) Def
c) Fun
d) Define"""
q6 = """What is the order of precedence in python?
a) Exponential, Parentheses, Multiplication, Division, Addition, Subtraction
b) Exponential, Parentheses, Division, Multiplication, Addition, Subtraction
c) Parentheses, Exponential, Multiplication, Division, Subtraction, Addition
d) Parentheses, Exponential, Multiplication, Division, Addition, Subtraction"""
q7 = """ What does pip stand for python?
a) unlimited length
b) all private members must have leading and trailing underscores
c) Preferred Installer Program
d) none of the mentioned"""
q8 = """ Which of the following is not a core data type in Python programming?
a) Tuples
b) Lists
c) Class
d) Dictionary"""
q9 = """Which of these is the definition for packages in Python?
a) A set of main modules
b) A folder of python modules
c) A number of files containing Python definitions and statements
d) A set of programs making use of Python modules"""
q10 =""" What arithmetic operators cannot be used with strings in Python?
a) *
b) -
c) +
d) All of the mentioned"""

answers_sheet = {q1: "c", q2: "a", q3: "c", q4: "a", q5: "b", q6: "d", q7: "c", q8: "c", q9: "b", q10: "b"}

dictToList = list(answers_sheet.keys())
random.shuffle(dictToList)

candidate_name = input("Enter Your Name: ")
print("Welcome,", candidate_name, "This is the Game of Knowledge", "\n")

a = input("Please Select Yes(Y) for Start a quiz: ").lower()

if a == "y" or "yes":
    instructions = """-----INSTRUCTIONS-----
1.No use of additional applications or internet
2.No cell phones or other secondary devices in the room or test area
3.Close all browsers/tabs before starting the quiz.
4.No negative Marking
5.Compulsary to attemp all questions"""

    print(instructions, "\n")
    score = 0
    for i in dictToList:
        print(i)
        flag1 = input("Do you want to skip the questions? (yes/no)").lower()
        if flag1 == "yes" or "y":
            continue
        else:
            ans = input("Enter the correct answer (a/b/c/d):").lower()
            if ans == answers_sheet[i]:
                print("Correct!")
                score += 1
            else:
                print("Wrong!")
    if score >= 9:
        print("Excellent! You are in Good Path! :)")
    elif score >= 6:
        print("Good! Better to Improve!")
    else:
        print("Poor! Please Work Hard")
    print("Your Final Score is :", score)

else:
    quit()