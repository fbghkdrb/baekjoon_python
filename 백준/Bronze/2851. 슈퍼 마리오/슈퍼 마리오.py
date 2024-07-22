li = [int(input()) for _ in range(10)]
point = 0
count = 100
max_index = 0

for i in range(10) :
    point += li[i]
    if point >= 100 :
        max_index = i
        break

if point - 100 == 0 :
    print(100)
elif point - 100 <= 100 - (point - li[max_index]) :
    print(point)
else :
    print(point - li[max_index])
