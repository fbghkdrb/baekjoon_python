def solution(arr):
    stk = [arr[0]]
    for i in range(1, len(arr)) :
        while stk and stk[-1] >= arr[i] :
            stk.pop(-1)
        stk.append(arr[i])
    return stk