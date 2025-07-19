def solution(number):
    num = 0
    for i in str(number) :
        num += int(i)
    return num % 9