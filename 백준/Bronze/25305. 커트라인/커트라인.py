N, k = map(int, input().split())
li = list(map(int, input().split()))

for i in range(N) :
    for j in range(N-1-i) :
        if li[j] > li[j+1] :
            temp = li[j]
            li[j] = li[j+1]
            li[j+1] = temp

print(li[-k])