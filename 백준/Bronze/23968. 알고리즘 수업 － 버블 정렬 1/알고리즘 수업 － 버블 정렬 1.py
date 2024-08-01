N, K = map(int, input().split())
A = list(map(int, input().split()))
count = 0
found = False

for i in range(N) :
    for j in range(N-1-i) :
        if A[j] > A[j+1] :
            temp = A[j]
            A[j] = A[j+1]
            A[j+1] = temp
            count += 1
            if count == K :
                print(A[j], A[j+1])
                found = True
                break
    if found :
        break

if count < K :
    print(-1)
