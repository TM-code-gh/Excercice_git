from math import *

student_A = {'name':'Toto','grades':[20, 15, 12, 10]}
student_B = {'name':'Mimi','grades':[12, 12, 12, 15]}
student_C = {'name':'Dada','grades':[6, 20, 10, 2]}

students=[student_A, student_B, student_C]


def mean(student):
    return {'name':student['name'], 'mean':sum(student['grades'])/len(student['grades'])}

def ranking_student(students):
    students_mean = []

    for student in students:
        students_mean.append(mean(student))
    
    return students_mean

def define_teacher(student, teacher):
    student['teacher'] = teacher

to_rank = ranking_student(students)
define_teacher(student_A, "Jean DUPONT")