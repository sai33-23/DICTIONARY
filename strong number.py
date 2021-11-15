# num=int(input("enter a number"))
# temp=num
# sum=0
# while num>0:
#     i=1
#     j=1
#     c=num%10
#     while i<=c:
#         j=j*i
#         i=i+1
#         sum=sum+j
#         num=num//10
# if temp==sum:
#     print("strong")
# else:
#     print("not")


n=int(input('enter no.'))
a=n
sum=0
while n>0:
	i=1
	f=1
	b=n%10
	while i<=b:
		f=f*i
		i+=1
	sum=sum+f
	n=n//10
if a==sum:
	print('strong no')
else:
	print('weak no')