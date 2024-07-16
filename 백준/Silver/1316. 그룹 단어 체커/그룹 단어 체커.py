N = int(input())
li = [input() for _ in range(N)]
count = 0

for i in li:
    li2 = ''
    is_group_word = True
    for j in range(len(i) - 1):
        if i[j] != i[j+1]:
            li2 = i[j+1:]
            if i[j] in li2:
                is_group_word = False
                break
    if is_group_word:
        count += 1

print(count)