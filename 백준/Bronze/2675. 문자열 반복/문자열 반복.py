t=int(input())
for _ in range(t):
    r,sen=input().split()
    p=''
    r=int(r)
    for s in sen:
        p+=r*s
    print(p)