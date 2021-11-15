i=1
n=int(input("enter a number"))
while i<=n:
    f=0
    a=1
    while a<=n:
        if i%a==0:
            f=f+1
        a=a+1
    if f==2:
        print(i)
    i=i+1