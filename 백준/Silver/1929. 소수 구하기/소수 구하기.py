M, N = map(int, input().split())

a = [False,False] + [True]*(N-1) #a[0], a[1]은 소가 아님 (False) / 나머지는 True
primes=[]

for i in range(2,N+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, N+1, i):
        a[j] = False

    if i >= M :
       print(i)