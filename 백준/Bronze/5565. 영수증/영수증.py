n=int(input()) #총 가격
sum=0
for i in range(9):
    price=int(input())
    sum+=price
print(n-sum)