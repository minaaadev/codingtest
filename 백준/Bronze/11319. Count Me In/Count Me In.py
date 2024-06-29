

moeum=['A','E','I','O','U','a','e','i','o','u']

for i in range(int(input())):
    sen=input()
    ja=0
    mo=0
    for s in sen:
        if s in moeum:
            mo+=1
        elif s.isalpha():
            ja+=1
    print(ja, mo)
