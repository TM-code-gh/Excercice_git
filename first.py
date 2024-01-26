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
        create(value)
        
show()
create(['A','B','C','C*','D','E','F','F*','F**','G','H'])

def moyenne(values):
    return sum(values)/len(values)


print(moyenne([20, 15, 12, 10]))
print(moyenne([12, 12, 12, 15]))