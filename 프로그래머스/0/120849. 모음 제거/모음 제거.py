def solution(my_string):
    answer=''
    moeum=('a,e,i,o,u')
    for mo in moeum:
        my_string= my_string.replace(mo,'')
    return my_string