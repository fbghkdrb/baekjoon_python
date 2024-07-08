X = input()
count = 0
    
def sum_of_x(num):
    result = 0
    for i in str(num):
        result += int(i)
    return result

while len(X) != 1 :
    X = str(sum_of_x(X))
    count += 1

print(count)

if int(X) % 3 == 0:
    print("YES")
else:
    print("NO")
