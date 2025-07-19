def solution(a, b, c, d):
    answer = 0
    arr = [a, b, c, d]
    temp = [0] * 6
    arr.sort()
    for i in arr :
        temp[i-1] += 1
    if 4 in temp :
        answer = 1111 * (temp.index(4) + 1)
    elif 3 in temp :
        answer = (10 * (temp.index(3) + 1) + (temp.index(1) + 1)) ** 2
    elif 2 in temp :
        if temp.count(2) == 2 :
            ind = list(filter(lambda x: temp[x] == 2, range(len(temp))))
            answer = ((ind[1] + 1) + (ind[0] + 1)) * ((ind[1] + 1) - (ind[0] + 1))
        else :
            ind = list(filter(lambda x: temp[x] == 1, range(len(temp))))
            answer = (ind[1] + 1) * (ind[0] + 1)
    else :
        answer = temp.index(1) + 1
    return answer