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

