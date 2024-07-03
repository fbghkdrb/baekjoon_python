def reverse() :
    num = int(input())
    reversed_num = int(str(num)[::-1])

    result = num + reversed_num
    reversed_result = int(str(result)[::-1])

    if result == reversed_result :
        print("YES")
    else :
        print("NO")

T = int(input())
for i in range (T) :
    reverse()
