def scramble(): # Prints out a scramble.
    from random import randint
    moves = ['U','D','R','L','F','B']
    ways = ['',"'",'2']
    opposites = {'U':'D','D':'U','F':'B','B':'F','L':'R','R':'L'}
    two_axial_turns = False
    last_move = ''
    m = moves[randint(0,5)]
    for x in range(28):
        moves.remove(m)
        print(m+ways[randint(0,2)],end=' ')
        last_move = m
        m = moves[randint(0,4)]
        while (two_axial_turns) and opposites[last_move] == m:
            m = moves[randint(0,4)]
        two_axial_turns = (opposites[last_move] == m)
        moves = ['U','D','R','L','F','B']


def stopwatch():
    from timeit import timeit
    def time():
        input()
    clock = timeit(time,number=1)
    return clock

def rubik(): # Does a practice solve, without affecting stats.
    scramble()
    input('\nPress enter to start/stop.')
    return stopwatch()

def average(*args): # Prints out the average of all recorded times.
    if len(args) == 0:
        from statistics import mean
        return mean(encapsulate())
    elif number() < args[0]:
        return 'Not enough solves'
    else:
        times = encapsulate()
        average = 0
        how_many = args[0]
        for x in range(len(times)-1,len(times)-(how_many+1),-1):
            average += times[x]/how_many
        return average
        

def times(): # Prints out all your times.
    file = open('rubikstimes.txt',mode='r')
    print(file.read())

def encapsulate():
    file = open('rubikstimes.txt',mode='r')
    lines = file.read()
    return list(map(float, lines.split(',')))

def solve(): # Same as rubik(), but DOES affect stats.
    file = open('rubikstimes.txt',mode='a')
    time = str(rubik())
    print(time)
    file.write(','+time)
    file.close()

def best(): # Returns best time
    return min(encapsulate())

def worst(): # Returns worst time
    return max(encapsulate())

def number(): # Return number of solves
    return len(encapsulate())

def graph(): # Shows a graph to you.
    from turtle import xcor,penup,goto,pendown,dot,ht,speed,pencolor,width
    penup()
    ht()
    speed(0)
    goto(-300,300)
    times = encapsulate()
    step = 600/len(times)
    for time in range(len(times)):
        goto(xcor()+step,times[time]*10-300)
        pendown()
        dot(5)
    penup()
    pencolor('red')
    goto(-300+step*2,300)
    width(2)
    for x in range(2,len(times)-2):
        mA5 = (times[x-2]+times[x-1]+times[x]+times[x+1]+times[x+2])/5
        goto(xcor()+step,mA5*10-300)
        pendown()
        
def stats():
    print('Best time: '+str(best()))
    print('Worst time: '+str(worst()))
    print('Session Average: '+str(average()))
    print('Current average of 5: '+str(average(5)))
    print('Current average of 12: '+str(average(12)))
    print('Number of solves: '+str(number()))
    
