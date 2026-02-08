l = [int(input()) for _ in range(9)]
answer = sum(l)
found = False

for i in range(9):
    for j in range(i + 1, 9):
        if answer - l[i] - l[j] == 100:
            val1, val2 = l[i], l[j]
            l.remove(val1)
            l.remove(val2)
            found = True
            break
    if found:
        break

l.sort()
for n in l:
    print(n)