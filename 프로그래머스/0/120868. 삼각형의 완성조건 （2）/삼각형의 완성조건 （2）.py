def solution(sides):
    answer = 0
    for i in range(1, 10000) :
        if i <= max(sides) : #max가 가장 클 때
            if max(sides) < min(sides) + i:
                answer += 1
        elif i >= max(sides) : #i가 가장 클 때
            if i < sum(sides) :
                answer += 1
    return answer


'''
1. 배열 안의 max 값이 최대값인 경우 : max(sides) < sum(sides) - max(sides) 를 for문을 돌려 answer += 1
2. 나머지 변이 최대값인 경우 : i < sum(sides)를 for 문을 돌려 answer += 1
'''