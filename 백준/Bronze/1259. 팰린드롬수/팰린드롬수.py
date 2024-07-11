text = ''
while text != '0' :
    text = input()
    reversed_text = text[::-1]
    if text == '0' :
        break
    if text == reversed_text :
        print("yes")
    else :
        print("no")