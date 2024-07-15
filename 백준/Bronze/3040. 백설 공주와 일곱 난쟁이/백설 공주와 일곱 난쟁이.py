li = [int(input()) for _ in range(9)]

num = sum(li) - 100

for i in range(8) :
    for j in range(i + 1, 9) :
        if li[i] + li[j] == num :
            index1, index2 = i, j
            break

if index1 < index2:
    del li[index2]
    del li[index1]
else:
    del li[index1]
    del li[index2]

for k in range(7) :
    print(li[k])