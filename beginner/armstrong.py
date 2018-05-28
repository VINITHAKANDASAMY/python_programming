n=int(input())
sum=0
temp=n
while temp > 0:
   digit = temp % 10
   sum+= digit ** 3
   temp//= 10
if n==sum:
   print("Armstrong number:yes")
else:
   print(" not an Armstrong number:no")
