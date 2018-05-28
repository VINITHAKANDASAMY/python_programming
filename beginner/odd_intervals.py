i=int(input())
n=int(input())
if(i and n<=100000):
  for a in range(i,n):
   if((a%2)!=0):
     if(a>i):
       print(a)
else:
  print("no")
