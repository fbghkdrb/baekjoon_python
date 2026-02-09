a = int(input())
l = list(map(int, input().split()))
count = 0

for i in l :
    if i == 1 :
        continue
    tf = True
    for j in range(2, i) :
        if i % j == 0 :
            tf = False
            break
    if tf == True :
        count += 1

print(count)