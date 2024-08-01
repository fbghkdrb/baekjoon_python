N = int(input())
li = [int(input()) for _ in range(N)]

for i in range(N) :
    for j in range(len(li) - 1 - i) :
        if li[j] > li[j+1] :
            temp = li[j]
            li[j] = li[j+1]
            li[j+1] = temp

for n in li :
    print(n)