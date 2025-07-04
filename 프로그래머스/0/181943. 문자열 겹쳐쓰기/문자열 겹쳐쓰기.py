def solution(my_string, overwrite_string, s):
    answer = ''
    for i in range(len(my_string)) :
        if i < s :
            answer += my_string[i]
            
    answer += overwrite_string
    
    for j in range(len(my_string)) :
        if j >= s + len(overwrite_string) :
            answer += my_string[j]
            
    return answer