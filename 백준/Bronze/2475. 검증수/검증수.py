gum=0
nums=list(map(int,input().split()))
for num in nums:
    gum+=num**2
print(gum%10)