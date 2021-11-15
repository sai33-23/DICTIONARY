n=int(input("enter a number"))
rev=0
i=n
while n>0:
    digit=n%10
    rev=rev*10+digit
    rev=n//10
    if i==rev:
        print("palindrome")
    else:
        print("not")