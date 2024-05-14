n=int(input())
for _ in range(n):
    string=list(input().split())
    for s in string:
        print(s[::-1], end=' ')