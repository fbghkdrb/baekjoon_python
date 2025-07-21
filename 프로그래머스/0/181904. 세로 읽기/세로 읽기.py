def solution(my_string, m, c):
    answer = []
    print(len(my_string))
    for i in range(int(len(my_string)/m)) :
        answer.append(my_string[i*m:i*m+m][c-1:c])
    return ''.join(answer)

# 0~4 / 5~8 / 9~12 / 13~16