n = int(input())
a = list(map(int, input().split()))
b = [0] * n

new_a = list(enumerate(a))
new_a.sort(key=lambda x: x[1])

for i, (index, value) in enumerate(new_a):
    b[index] = i

print(*b)
