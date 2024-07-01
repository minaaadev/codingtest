def solution(array, n):
    answer = 0
    
    if n in array:
        return array.count(n)
    else:
        return 0
    return answer