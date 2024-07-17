def solution(money):
    answer = []
    ameri=money//5500
    change=money%5500
    answer=[ameri,change]
    return answer