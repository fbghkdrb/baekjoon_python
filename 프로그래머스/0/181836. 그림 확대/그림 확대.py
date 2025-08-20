def solution(picture, k):
    answer = []
    for i in picture :
        a = ''
        for j in range(len(i)) :
            a += i[j] * k
        for n in range(k) :
            answer.append(a)
    return answer