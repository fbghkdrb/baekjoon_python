n = list(map(int, input()))

for i in range(0, len(n)-1) :
    for j in range(i+1, len(n)) :
        if n[j] > n[i] :
            temp = n[j]
            n[j] = n[i]
            n[i] = temp

print(*n, sep='')