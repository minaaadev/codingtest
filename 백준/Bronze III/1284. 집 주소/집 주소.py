while True:
    num=list(map(int,list(input())))
    
    if len(num)==1 and num[0]==0:
        break
        
    sum=1+len(num)
    
    for n in num:
        if n==0:
            sum+=4
        elif n==1:
            sum+=2
        else:
            sum+=3
    print(sum)