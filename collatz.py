from __future__ import print_function
import sys
import math
from turtle import *
import random

def eprint(thing):
    print(thing, file=sys.stderr)

def collatz(n,output='yes'):
    list0 = []
    while n != 1:
        list0.append(n)
        if n>>1<<1 == n:
            if output == 'yes':
                print(n)
            n = n >> 1
        else:
            if output == 'yes':
                eprint(n)
            n = 3*n+1
    if output == 'yes':
        print(1)
    return list0

def diagram(n):
    start = n
    list0 = []
    while n >= start:
        list0.append(n)
        if n>>1<<1 == n:
            print('D')
            n = n >> 1
        else:
            eprint('U')
            n = 3*n+1
    
def log_collatz_graph(n):          
    penup()
    goto(-400,-200)
    data = collatz(n,output='no')
    interval_width = 800/len(data)
    max_height = math.log(max(data))
    for x in range(len(data)):
        goto(xcor()+interval_width,(400/max_height)*math.log(data[x])-200)
        pendown()

def lin_collatz_graph(n):
    penup()
    goto(-400,-200)
    data = collatz(n,output='no')
    interval_width = 800/len(data)
    max_height = (max(data))
    for x in range(len(data)):
        goto(xcor()+interval_width,(400/max_height)*(data[x])-200)
        pendown()
        
collatz(27198375098123605813903485)
