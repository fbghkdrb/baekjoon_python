li = [int(input()) for _ in range(5)]

def mean_num(li) :
    sum = 0
    for i in li :
        sum += i
    
    return sum // 5

def middle_num(li) :
    for i in range(5) :
        for j in range(4 - i) :
            if li[j] > li[j+1] :
                temp = li[j]
                li[j] = li[j+1]
                li[j+1] = temp

    return li[2]

print(mean_num(li))
print(middle_num(li))
