n = int(input())
a = list(map(int, input().split()))
sum = 0
result = 0

a.sort()

for i in a :
    sum += i
    result += sum

print(result)