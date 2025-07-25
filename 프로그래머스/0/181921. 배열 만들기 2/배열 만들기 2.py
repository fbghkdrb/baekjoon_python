def solution(l, r):
    answer = []
    for i in range(l, r+1) :
        count = 0
        for j in str(i) :
            if '5' in j or '0' in j :
                count += 1
        if len(str(i)) == count :
            answer.append(i)
    if not answer :
        answer.append(-1)
    return answer