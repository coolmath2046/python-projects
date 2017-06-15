def floodfill(surface, x, y, oldColor=None, newColor=0):
    global visited, armyData, regionValue, armies
    rows = len(surface)
    columns = len(surface[0])
    if x > -1 and y > -1:
        try:
            if oldColor is None:
                oldColor = surface[x][y]
            if surface[x][y] != oldColor: # the base case
                return
            surface[x][y] = newColor
            if regionValue in armyData:
                armyData[regionValue] += armies[x][y]
            else:
                armyData[regionValue] = armies[x][y]
            visited[x][y] = newColor
        except IndexError:
            return
        floodfill(surface,x + 1, y, oldColor, newColor) # right
        floodfill(surface,x - 1, y, oldColor, newColor) # left
        floodfill(surface,x, y + 1, oldColor, newColor) # down
        floodfill(surface,x, y - 1, oldColor, newColor) # up
		

		
s = [['green', 'orange', 'orange', 'purple', 'green', 'orange', 'orange', 'orange', 'purple', 'purple', 'green', 'purple', 'green', 'purple', 'orange', 'green'], ['orange', 'green', 'green', 'green', 'orange', 'green', 'orange', 'green', 'green', 'orange', 'orange', 'orange', 'purple', 'green', 'green', 'orange'], ['orange', 'orange', 'orange', 'purple', 'orange', 'green', 'green', 'orange', 'green', 'purple', 'green', 'green', 'green', 'green', 'purple', 'green'], ['orange', 'purple', 'orange', 'purple', 'orange', 'green', 'purple', 'purple', 'orange', 'orange', 'green', 'green', 'purple', 'purple', 'orange', 'green'], ['purple', 'orange', 'orange', 'orange', 'orange', 'green', 'green', 'purple', 'green', 'orange', 'orange', 'green', 'green', 'green', 'green', 'orange'], ['orange', 'purple', 'purple', 'orange', 'purple', 'green', 'green', 'orange', 'green', 'green', 'green', 'purple', 'green', 'purple', 'purple', 'green'], ['orange', 'orange', 'purple', 'purple', 'purple', 'orange', 'orange', 'green', 'purple', 'green', 'orange', 'green', 'green', 'orange', 'orange', 'purple'], ['green', 'orange', 'orange', 'orange', 'purple', 'green', 'green', 'orange', 'green', 'green', 'purple', 'green', 'orange', 'green', 'purple', 'orange'], ['purple', 'orange', 'green', 'purple', 'green', 'orange', 'green', 'green', 'purple', 'green', 'green', 'orange', 'purple', 'purple', 'purple', 'green'], ['orange', 'purple', 'purple', 'green', 'green', 'purple', 'green', 'orange', 'green', 'purple', 'purple', 'orange', 'orange', 'orange', 'purple', 'purple'], ['green', 'orange', 'orange', 'green', 'orange', 'green', 'green', 'green', 'purple', 'green', 'green', 'orange', 'purple', 'orange', 'orange', 'purple'], ['purple', 'green', 'green', 'green', 'green', 'purple', 'purple', 'green', 'orange', 'green', 'green', 'purple', 'purple', 'purple', 'purple', 'orange'], ['green', 'purple', 'orange', 'orange', 'green', 'green', 'purple', 'purple', 'orange', 'orange', 'green', 'purple', 'orange', 'purple', 'orange', 'purple'], ['green', 'orange', 'green', 'green', 'green', 'green', 'orange', 'green', 'purple', 'green', 'green', 'purple', 'orange', 'purple', 'purple', 'purple'], ['purple', 'green', 'green', 'orange', 'purple', 'purple', 'purple', 'green', 'green', 'purple', 'green', 'purple', 'green', 'green', 'green', 'purple'], ['green', 'purple', 'orange', 'green', 'orange', 'green', 'orange', 'orange', 'purple', 'purple', 'purple', 'green', 'orange', 'purple', 'purple', 'green']]

armies = [[4, 5, 3, 4, 1, 7, 4, 5, 5, 7, 7, 2, 5, 1, 5, 6], [3, 2, 2, 5, 1, 5, 6, 7, 6, 5, 3, 6, 6, 3, 3, 6], [2, 4, 3, 6, 3, 6, 6, 3, 4, 2, 5, 3, 3, 3, 5, 6], [4, 5, 2, 4, 6, 2, 3, 5, 7, 4, 3, 4, 5, 5, 6, 8], [7, 3, 5, 4, 5, 4, 2, 5, 4, 3, 2, 8, 7, 3, 8, 6], [1, 6, 2, 5, 5, 2, 4, 2, 2, 4, 3, 4, 7, 1, 3, 4], [3, 5, 2, 6, 7, 6, 1, 2, 5, 4, 1, 5, 1, 5, 3, 6], [2, 2, 2, 3, 4, 4, 4, 7, 1, 7, 4, 6, 4, 5, 5, 4], [4, 5, 5, 4, 6, 4, 7, 1, 7, 4, 4, 4, 3, 2, 2, 2], [6, 3, 5, 1, 5, 1, 4, 5, 2, 1, 6, 7, 6, 2, 5, 3], [4, 3, 1, 7, 4, 3, 4, 2, 2, 4, 2, 5, 5, 2, 6, 1], [6, 8, 3, 7, 8, 2, 3, 4, 5, 2, 4, 5, 4, 5, 3, 7], [8, 6, 5, 5, 4, 3, 4, 7, 5, 3, 2, 6, 4, 2, 5, 4], [6, 5, 3, 3, 3, 5, 2, 4, 3, 6, 6, 3, 6, 3, 4, 2], [6, 3, 3, 6, 6, 3, 5, 6, 7, 6, 5, 1, 5, 2, 2, 3], [6, 5, 1, 5, 2, 7, 7, 5, 5, 4, 7, 1, 4, 3, 5, 4]]

temp = s
visited = [[0 for i in range(16)] for j in range(16)]
regionValue = 0
armyData = {}
for x in range(16):
    for y in range(16):
        if s[x][y] in ['orange','purple','green']:
            floodfill(s,x,y,None,str(regionValue))
            regionValue += 1
searchFor = [(index, row.index(val)) for index, row in enumerate(mymatrix) if val in row]

print(s)
print('\nArmies:')
print(armyData)
