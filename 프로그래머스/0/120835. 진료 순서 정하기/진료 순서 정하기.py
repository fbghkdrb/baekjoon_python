def solution(emergency):
    answer = []
    l = sorted(emergency)
    l.reverse()
    for i in range(len(emergency)) :
        answer.append(l.index(emergency[i]) + 1)
    return answer