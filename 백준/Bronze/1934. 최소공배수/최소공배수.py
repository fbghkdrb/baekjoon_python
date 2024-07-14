T = int(input())
a = [list(map(int, input().split())) for _ in range(T)]

for i in range(T) :
    gcd = 1
    for j in range(1, min(a[i][0], a[i][1]) + 1) :
        if a[i][0] % j == 0 and a[i][1] % j == 0 :
            gcd = j

    print((a[i][0] * a[i][1]) // gcd)
