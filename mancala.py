# Mancala
import time
cpu  = [0,4,4,4,4,4,4]
player = [4,4,4,4,4,4,0]
board = [cpu,player]
def print_board():
    if board[0][0] <= 9:
        print('\n' + str(cpu) + '\n   ' + str(player))
    else:
        print('\n' + str(cpu) + '\n    ' + str(player))

def add(x,a,b):
    board[a][b] = board[a][b]+x

def take_all(a,b):
    board[a][b] = 0

def next_hole_player(c,d):
    if c == 0 and d == 1:
        return (1,0)
    elif c == 1 and d == 6:
        return (0,6)
    elif c == 0:
        return (c,d-1)
    else:
        return (c,d+1)

def next_hole_cpu(c,d):
    if c == 0 and d == 0:
        return (1,0)
    elif c == 1 and d == 5:
        return (0,6)
    elif c == 0:
        return (c,d-1)
    else:
        return (c,d+1)

def move(e,f,who='player'):
    if who == 'player':
        row = 6-f
    else:
        row = 7-f
    current = (e,row)
    marbles = board[e][row]
    take_all(e,row)
    for i in range(marbles):
        if who == 'player':
            add(1,next_hole_player(current[0],current[1])[0],next_hole_player(current[0],current[1])[1]) # Good luck finding out what THIS line does!
            current = next_hole_player(current[0],current[1])
        else:
            add(1,next_hole_cpu(current[0],current[1])[0],next_hole_cpu(current[0],current[1])[1])
            current = next_hole_cpu(current[0],current[1])
    steal_status = board[current[0]][current[1]]
    if steal_status == 1 and (current[0],current[1]) != (0,0) and (current[0],current[1]) != (1,6):
        steal(current[0],current[1],who)
    print()
    if (current[0],current[1]) == (0,0) or (current[0],current[1]) == (1,6):
        if who == 'player':
            move(1,ask('player'),'player')
        else:
            move(0,ai(),'cpu') # todo: make an ai() function and change ask() to ai()

def steal(g,h,who='player'):
    if board[g][h] != 1:
        print('Something has gone wrong...')
        quit()
    if (who == 'player' and g == 1) or (who == 'cpu' and g == 0):
        if g == 0:
            if board[1][h-1] != 0:
                add(1+board[1][h-1],0,0)
                take_all(1,h-1)
                add(-1,g,h)
        else:
            if board[0][h+1] != 0:   
                add(1+board[0][h+1],1,6)
                take_all(0,h+1)
                add(-1,g,h)

def ai(): # Easy ai
    print_board()
    print('\n    1  2  3  4  5  6')
    time.sleep(1.5)
    for x in range(1,6):
        if cpu[x] == x:
            print('Ai moves from slot '+str(x))
            return 7-x
    for x in range(1,6):
        if cpu[x] > 0:
            print('Ai moves from slot '+str(x))
            return 7-x
    print('Ai moves from slot 1')
    return 1

def ask(who):
    print_board()
    print('\n    6  5  4  3  2  1')
    answer = 0
    while float(answer)%1 != 0 or int(answer) < 1 or int(answer) > 6:
        answer = input('What number do you want to move from, ' + who + '? ')
    return int(answer)                             

while board[0][0] + board[1][6] < 48:
    move(0,ai(),'cpu')
    move(1,ask('player'),'player')
print_board()

print('Player got ' + str(board[1][6]) + ' points, and cpu got ' + str(board[0][0]) + ' points.')
if board[0][0] > board[1][6]:
    print('cpu won!')
else:
    print('player won!')
