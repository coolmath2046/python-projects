grid = [[3,0,0,0],
        [2,0,0,0],
        [1,0,1,0],
        [0,0,2,0]]

def print_grid():
    for row in grid:
        print(row)

def up_barriers():
    up = []
    def index(r,c):
        return grid[row][column]
    for row in range(4):
        for column in range(4):
            if row == 0:
                up.append((0,column))
            elif index(row,column)+index(row-1,column) != 3: # Ones and twos
                
                
                
                
            
        

