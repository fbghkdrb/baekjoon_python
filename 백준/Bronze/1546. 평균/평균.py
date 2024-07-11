N = int(input())
current_score = list(map(int, input().split()))
max_score = max(current_score)
total = 0

for i in current_score :
    new_score = i / max_score * 100
    total += new_score

mean = total / N
print(mean)
