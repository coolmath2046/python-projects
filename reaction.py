import time
from random import random
def rank(time):
    if time < 0.18:
        return 'Reflex Wizard!'
    elif time < 0.21:
        return 'Lickety Split!'
    elif time < 0.23:
        return 'Quick Fingers!'
    elif time < 0.3:
        return 'Mediocre Medley'
    else:
        return 'Slow Joe'
def reaction():
    print('Sequence initiated. Keep your finger above Enter.')
    time.sleep(random()*3+1)
    tic = time.process_time()*60
    input('PRESS ENTER ASAP!')
    toc = time.process_time()*60
    rtime = round(toc-tic,5)
    print(toc)
    print('Reaction Time: ' + str(rtime))
    print('Rank: ' + rank(rtime) + '\n')
while True:
    reaction()
    time.sleep(1)
