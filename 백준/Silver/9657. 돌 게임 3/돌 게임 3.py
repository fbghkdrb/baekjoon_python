N = int(input())

dp = [0] * 1001

dp[1] = 1
dp[3] = 1
dp[4] = 1

for i in range(5, N+1) :
    if dp[i-1] and dp[i-3] and dp[i-4] == 1 :
        dp[i] = 0
    else : 
        dp[i] = 1

if dp[N] != 1 :
    print("CY")
else :
    print("SK")

'''
규칙성 찾기
전체에서 상근이 뽑는 경우 : 1, 3, 4개
>> 7 > 3, 4, 6
2의 경우 창영의 승

전체 - 1, 3, 4
아래에서 위로 올라가면서 확인

0 : 창영 승
1 : 상근 승
[0, 1, 0, 1, 1, 1, 1]
'''