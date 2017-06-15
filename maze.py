from turtle import *
from random import *
def trail(size,clear=1,pan=1,times=9999999999,vis=[],needto=[]):
    hideturtle()
    visited = vis
    ct = 0
    tc = 0
    are = 0
    need_to_visit = needto
    yo_man = 600 - 600%size
    unit = round(yo_man/size)
    minimum = -4
    begin_fill()
    if clear == 1:
        goto(-319,-319)
        fillcolor('black')
        begin_fill()
        for y in range(0,4):
            fd(yo_man + 27 -(unit))
            left(90)
        end_fill()
        yo_man = yo_man - unit
        goto(-299,-299)
        pencolor('white')
        fillcolor('red')
        begin_fill()
        for u in range(0,4):
            fd(10)
            left(90)
        end_fill()
    width(unit/3)
    while xcor() < 298-unit and ycor() < 298-unit and tc < times:
        if ct > 24:
            pencolor('black')
            if clear == 1:
                for r in range(0,5):
                    goto(visited[len(visited)-2])
                    visited.remove(visited[len(visited)-2])
                    need_to_visit.remove(need_to_visit[len(need_to_visit)-2])
            pencolor('white')
        delay(0)
        if clear == 1:
            ranlist = [0,0,0,0,90,90,90,90,-90,-90,180,180]
        else:
            ranlist = [-90,90,0,90,0,180,-90,180,-90,90,0,180]
        ran = randint(0,11)
        seth(ranlist[ran])
        penup()
        fd(unit)
        position = (round(xcor()),round(ycor()))
        tc = tc + 1
        if xcor() > -300 and xcor() < 300-(unit)+(clear*unit) and ycor() > -300 and ycor() < 300-(unit)+(clear*unit) and position not in visited:
            back(unit)
            pendown()
            fd(unit)
            penup()
            visited.append(position)
            need_to_visit.append(position)
            ct = 0
        else:
            back(unit)
            ct = ct + 1
    begin_fill()
    if clear == 1:
        for u in range(0,4):
            fillcolor('green')
            fd(10)
            left(90)
        end_fill()
    if clear == 1:
        while len(visited) < (size) * (size) - 1 - are:
            for a in range(0,len(need_to_visit),1):
                ind = need_to_visit[a]
                goto(ind)
                print(len(need_to_visit))
                print(len(visited))
                print('\n\n')
                if (ind[0]-unit,ind[1]) in visited and (ind[0]+unit,ind[1]) in visited and (ind[0],ind[1]-unit) in visited and (ind[0],ind[1]+unit) in visited:
                    need_to_visit.remove(ind)
                    are += 1
                trail(size,clear=0,times=randint(minimum*size,3*size),vis=visited,needto=need_to_visit)
                minimum = 0
        

trail(15)
goto(-192,318)
pencolor('black')
write('Mazeflash v1.0',font=('Arial',36,'normal'))
