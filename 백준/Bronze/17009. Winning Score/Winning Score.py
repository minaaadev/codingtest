apple=0
banana=0

num=[int(input()) for _ in range(3)]
a=num[0]*3+num[1]*2+num[2]
numm=[int(input())for _ in range(3)]
b=numm[0]*3+numm[1]*2+numm[2]

if a>b:
    print("A")
elif b>a:
    print("B")
else:
    print("T")