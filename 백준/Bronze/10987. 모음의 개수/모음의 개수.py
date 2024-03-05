sen=input()
dict={"a", "e", "i", "o","u","A","E","I","O","U"}
sum=0
for i in sen:
  if i in dict:
    sum+=1
print(sum)