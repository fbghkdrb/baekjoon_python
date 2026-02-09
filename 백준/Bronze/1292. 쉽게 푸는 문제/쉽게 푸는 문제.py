l = list(map(int, input().split()))
tot_max, tot_min = 0, 0
n = 0

for i in range(1, 1001):
    for j in range(i):
        n += 1
        if n < l[0]:
            tot_min += i
        if n <= l[1]:
            tot_max += i
        else:
            break
            
    if n > l[1]:
        break

print(tot_max - tot_min)