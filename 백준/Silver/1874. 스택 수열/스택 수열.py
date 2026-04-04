l = int(input())
n = []
for i in range(l) :
    n.append(i+1)
a = [int(input()) for _ in range(l)]
stack = []
answer = []
count = 1
no = False

for i in a :
    while count <= i :
        stack.append(count)
        answer.append('+')
        count += 1
    
    if stack[-1] == i :
        stack.pop()
        answer.append('-')
    
    else :
        no = True
    
if no :
    print("NO")
else :
    print('\n'.join(answer))