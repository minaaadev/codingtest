def solution(price):
    answer = 0
    if price>=100000 and price<300000:
        return int(price*(95/100))
    elif price>=300000 and price<500000:
        return int(price*(90/100))
    elif price>=500000:
        return int(price*(80/100))
    else:
        return int(price)
    return answer