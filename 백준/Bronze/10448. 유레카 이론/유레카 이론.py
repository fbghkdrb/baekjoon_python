from itertools import product

triangle_num = []
total = 0
for i in range(1, 9999):
    total += i
    triangle_num.append(total)

    if total > 1000:
        break

case = set(sum(x) for x in product(triangle_num, repeat=3))
case = sorted(case)

T = int(input())
for _ in range(T):
    K = int(input())
    for i in case:
        if K == i:
            print(1)
            break

        if K < i:
            print(0)
            break