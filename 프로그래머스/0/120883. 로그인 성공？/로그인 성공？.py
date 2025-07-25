def solution(id_pw, db):
    answer = ''
    for id, pw in db :
        if id_pw[0] == id and id_pw[1] != pw :
            answer = 'wrong pw'
            break
        elif id_pw[0] == id and id_pw[1] == pw :
            answer = 'login'
            break
        else :
            answer = 'fail'
    return answer