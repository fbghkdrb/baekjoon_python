def solution(x):
    answer = True
    temp = 0
    for i in range(len(str(x))) :
        temp += int(str(x)[i])
    if x % temp == 0 :
        return answer
    else :
        return False
    '''
    
    if len(str(x)) == 1 :
        return answer
    elif len(str(x)) == 2 :
        if x % (int(str(x)[0]) + int(str(x)[1])) == 0 :
            return answer
        else :
            return False
    '''