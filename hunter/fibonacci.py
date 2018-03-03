nterms = 5

a = 0
b = 1
total = 0

if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(a)
else:
   print("Fibonacci sequence upto",nterms,":")
   while total < nterms:
       print(a,end=' , ')
       nth = a + b
       # update values
       a = b
       b = nth
       total += 1
