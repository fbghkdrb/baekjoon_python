n = [int(input()) for _ in range(28)]
n.sort()

li = [0] * 30
i = 0
while i < 28 :
    li[n[i] - 1] += 1
    i += 1

for i in range(30) :
    if li[i] == 0 :
        print(i + 1)