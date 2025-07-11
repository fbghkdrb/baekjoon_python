def solution(my_str, n):
    answer = []
    for i in range(len(my_str)) :
        answer.append(my_str[0 + i*n : n + i*n])
    while "" in answer :
        answer.remove("")
    return answer