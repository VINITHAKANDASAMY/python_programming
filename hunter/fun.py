list = ['guvi'] 

def aa(x):
     print (x * 5)
 

def my_simple(fun, list):
     for item in list:
         fun(item)
 

my_simple(aa, list)
