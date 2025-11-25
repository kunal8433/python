from functools import reduce
# MAP 
l = [12,2,5,6,4]

square = lambda x: x*x

sqList = map(square, l)
print(list(sqList))

#FILTER 

def even (n):
     if (n%2 == 0 ):
          return True 
     return False

onlyEven = filter(even , l)
print(list(onlyEven))

# REDUCE 

def sum(a,b):
     return a+b 
print(reduce(sum,l))
