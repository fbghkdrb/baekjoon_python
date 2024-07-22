T = int(input())
for _ in range(T) :
    N = int(input())
    li = list(input().split() for _ in range(N))
    max_ = int(li[0][1])
    school = li[0][0]
    for j in li :
        if int(j[1]) > max_ :
            max_ = int(j[1])
            school = j[0]

    print(school)
