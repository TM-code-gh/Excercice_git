from math import *
from datetime import datetime

def show():
    print("Hello World")
    print("Hey you! Hello!!")
    print("Oh hello!!")

def show(value):
    print(value)

def create(values):
    for value in values:
        show(value)
        
show()
create(['A','B','C','C*','D','E','F','F*','F**','G','H'])

def mean(values):
    return sum(values)/len(values)

student_A_mean = mean([20, 15, 12, 10])
student_B_mean = mean([12, 12, 12, 15])

students_mean=[student_A_mean, student_B_mean]

def get_best_student(students_mean):
    best = students_mean[0]
    for student_mean in students_mean[1:]:
        if student_mean>best:
            best = student_mean
    return students_mean.index(best)
            
        
    
