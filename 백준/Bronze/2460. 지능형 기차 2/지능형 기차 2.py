l = [list(map(int, input().split())) for _ in range(10)]
n = 0
answer = 0
for i in range(10) :
    n -= l[i][0]
    n += l[i][1]
    if n > answer :
        answer = n

print(answer)