n = int(input())
for i in range(n) :
    a, b = input().split()
    sorted_a = ''.join(sorted(a))
    sorted_b = ''.join(sorted(b))
    if sorted_a == sorted_b :
        print(a, "&", b, "are anagrams.")
    else :
        print(a, "&", b, "are NOT anagrams.")