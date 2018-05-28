num=input("enter value:")
fact=1
if num < 0:
   print("negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       fact= fact*i
   print("factorial value is:")
   print(fact)
