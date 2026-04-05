def solution(progresses, speeds):
    answer = []
    arr = []
    for i in range(len(progresses)) :
        n = 1
        while (progresses[i] + n*speeds[i] < 100) :
            n += 1
        arr.append(n)
        
    top = -1
    cnt = 0
    for num in arr :
        if top == -1 :
            top = num
        elif top < num :
            cnt += 1
            answer.append(cnt)
            cnt = 0
            top = num
        else :
            cnt += 1
    answer.append(cnt+1)
            
    return answer