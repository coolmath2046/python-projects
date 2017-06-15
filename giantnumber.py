squareindex = 1
result = 3
string = ''

while squareindex <= 13:
    result = result*result
    squareindex += 1

result=str(result)
index=1
resultlen = len(result)

while index < resultlen:
    if result[index] == '0':
        string = string + "'"
    elif result[index] == '1':
        string = string + '"'
    elif result[index] == '2':
        string = string + '*'
    elif result[index] == '3':
        string = string + '-'
    elif result[index] == '4':
        string = string + 'i'
    elif result[index] == '5':
        string = string + 'I'
    elif result[index] == '6':
        string = string + '$'
    elif result[index] == '7':
        string = string + 'w'
    elif result[index] == '8':
        string = string + 'M'
    else:
        string = string + '#'
    index += 1

print(string)




    
