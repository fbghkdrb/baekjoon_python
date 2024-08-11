n = int(input())
li = list(int(input()) for _ in range(n))

li.sort(reverse=True)

for num in li :
    print(num)