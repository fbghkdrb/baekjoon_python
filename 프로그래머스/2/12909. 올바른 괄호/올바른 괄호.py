def solution(s):
    arr = []
    for ss in s :
        if arr == [] :
            arr.append(ss)
        elif ss == arr[-1] or (arr[-1] == ')' and ss != arr[-1]):
            arr.append(ss)
        else :
            arr.pop()
    if arr == [] :
        return True
    else :
        return False