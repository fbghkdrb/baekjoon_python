l = list(map(int, input().split()))
ans = []
for i in range(1, l[0]+1) :
    if l[0] % i == 0 :
        ans.append(i)
if len(ans) < l[1] :
    print(0)
else :
    print(ans[l[1]-1])