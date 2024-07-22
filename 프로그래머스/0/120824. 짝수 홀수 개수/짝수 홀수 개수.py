def solution(num_list):
    answer = []
    odd=0
    even=0
    for num in num_list:
        if num%2==0:
            even+=1
        elif num%2==1:
            odd+=1
            
    answer=even,odd
    return answer