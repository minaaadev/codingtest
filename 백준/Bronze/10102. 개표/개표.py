v=int(input())
votes=input().strip()
a_count=0
b_count=0

for vote in votes:
    if vote=='A':
        a_count+=1
    elif vote=='B':
        b_count+=1
    
        
if a_count>b_count:
    print("A")
elif a_count==b_count:
        print("Tie")
else:
    print("B")