n=int(input())
num=list(map(int, input().split()))

snum=sorted(num)
ans=0

for s in range(1,n+1):
    ans+=sum(snum[0:s])
print(ans)