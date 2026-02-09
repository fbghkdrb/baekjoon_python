a = int(input())
l = [list(map(int, input().split())) for _ in range(a)]
for i in range(len(l)) :
    l[i].sort()
    print(l[i][-3])