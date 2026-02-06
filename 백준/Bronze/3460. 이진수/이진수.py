n = int(input())
l = [int(input()) for _ in range(n)]
answer = []

for i in range(n) :
    b = str(format(l[i], 'b'))
    re_b = ''.join(reversed(b))
    for j in range(len(b)) :
        if re_b[j] == '1' :
            answer.append(j)

for i in range(len(answer)) :
    print(answer[i], end=' ')