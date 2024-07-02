def calculate_prize(dice):
    counts = [0] * 7
    for i in dice:
        counts[i] += 1
    
    if 4 in counts:
        value = counts.index(4)
        return 50000 + value * 5000
    elif 3 in counts:
        value = counts.index(3)
        return 10000 + value * 1000
    elif counts.count(2) == 2:
        pair_values = [i for i in range(1, 7) if counts[i] == 2]
        return 2000 + pair_values[0] * 500 + pair_values[1] * 500
    elif 2 in counts:
        value = counts.index(2)
        return 1000 + value * 100
    else:
        return max(dice) * 100

N = int(input())
max_prize = 0
    
for _ in range(N):
    dice = list(map(int, input().split()))
    prize = calculate_prize(dice)
    if prize > max_prize:
        max_prize = prize
    
print(max_prize)