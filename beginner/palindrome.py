n=int(input("Enter number:"))
temp=n
a=0
while(n>0):
    d=n%10
    a=a*10+d
    n=n//10
if(temp==a):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")

