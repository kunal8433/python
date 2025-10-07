def factriol(n):
    if(n==0 or n==1):
        return 1
    return n * factriol(n-1)

n = int(input("Enter your number:"))
print(f"the factriol of this number is : {factriol(n)}")
    
