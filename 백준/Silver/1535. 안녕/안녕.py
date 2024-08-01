N = int(input())
L = [0] + list(map(int, input().split()))
J = [0] + list(map(int, input().split()))
dp = list([0]*101 for _ in range(N+1))

for i in range(1,N+1):
    for j in range(1,101):
        if j<=L[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], J[i] + dp[i-1][j-L[i]])

print(dp[N][100])
