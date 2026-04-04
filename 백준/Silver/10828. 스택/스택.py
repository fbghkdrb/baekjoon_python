array = list()

def push(data) :
    array.append(data)

def pop() :
    if len(array) == 0 :
        return -1
    return array.pop()

def size() :
    return len(array)

def empty() :
    if len(array) == 0 :
        return 1
    else :
        return 0
    
def top() :
    if len(array) == 0 :
        return -1
    return array[-1]

l = int(input())
a = [input() for _ in range(l)]
for i in a :
    if i.startswith('push') :
        push(int(i.split()[1]))
    elif i.startswith('pop') :
        print(pop())
    elif i.startswith('size') :
        print(size())
    elif i.startswith('empty') :
        print(empty())
    elif i.startswith('top') :
        print(top())