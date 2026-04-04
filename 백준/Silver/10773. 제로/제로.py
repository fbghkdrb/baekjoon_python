array = list()

def push(data) :
    array.append(data)

def pop() :
    if len(array) == 0 :
        return -1
    else :
        array.pop()

l = int(input())
a = [int(input()) for _ in range(l)]
for i in a :
    if i == 0 :
        pop()
    else :
        push(i)

print(sum(array))