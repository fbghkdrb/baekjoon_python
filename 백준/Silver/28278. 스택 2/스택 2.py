N = int(input())
li = []

commands = [input().split() for _ in range(N)]

for command in commands :
    if command[0] == '5' :
        if li == [] :
            print(-1)
        else : 
            print(li[-1])
    elif command[0] == '3' :
        if li == [] :
            print(0)
        else :
            print(len(li))
    elif command[0] == '4' :
        if li == [] :
            print(1)
        else :
            print(0)
    elif command[0] == '2' :
        if li == [] :
            print(-1)
        else :
            num = li.pop()
            print(num)
    elif command[0] == '1' :
        li.append(command[1])