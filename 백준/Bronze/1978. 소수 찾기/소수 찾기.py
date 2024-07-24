N = int(input())
li = list(map(int, input().split()))
count = 0

for num in li :
    if num == 1 :
        continue
    if num == 2 :
        count += 1
        continue
    if_dec = True
    for i in range(2, num) :
        if num % i == 0 :
            if_dec = False
            break

    if if_dec == True :
        count += 1

print(count)