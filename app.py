from function import *
num = int(input("Enter the number of students you want to grade: "))
for i in range(num):
    name = input(f"Enter {i+1} your name: ")
    score = float(input("What is your score: "))
    scores(score)