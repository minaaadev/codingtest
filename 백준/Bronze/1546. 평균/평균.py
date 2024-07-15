n=int(input())
nums=list(map(int,input().split()))
big=max(nums)
ans=[]
for num in nums:
    ans.append(num/big*100)
    dap=sum(ans)/n
print(dap)