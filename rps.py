def rps():
    try:
        a = 'rock'
        b = 'paper'
        c = 'scissors'
        valid = [a,b,c]
        outcomes = {a:{a:0,b:-1,c:'smashes'},
                    b:{a:'covers',b:0,c:-1},
                    c:{a:-1,b:'cuts',c:0}}
        import random,time
        while True:
            player = ''
            while player not in valid:
                player = input('\nChoose a play. Valid plays: '+str(valid)+' Selection: ').lower()
            computer = valid[random.randint(0,2)]
            result = outcomes[player][computer]
            print('\nPlayer: '+player)
            print('Computer: '+computer+'\n')
            if player == computer:
                print("It's a tie!")
            elif result == -1:
                result = outcomes[computer][player]
                print(computer+' '+result+' '+player+'!')
                print('Computer Wins!')
            else:
                print(player+' '+result+' '+computer+'!')
                print('Player Wins!')
            if input('Want to play again?\n').lower()[0] == 'n':
                break
    except IndexError:
        rps()
rps()
