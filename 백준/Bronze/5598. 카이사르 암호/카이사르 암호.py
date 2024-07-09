text = input()
result = ""

for i in text :
    result += chr((ord(i) - ord('A') - 3) % 26 + ord('A'))

print(result)