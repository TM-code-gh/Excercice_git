from tkinter import *
from tkinter.messagebox import *
from math import *
import random
import pandas as pd
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


