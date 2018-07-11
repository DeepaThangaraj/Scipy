#compute the decimals of pi using Wallis formula
def wallis(iterator):
    pi=2.0 #according to the formula pi is initialized as 2.0 which gives decimal value
    for i in range(1,iterator):
        x=4*i**2
        y=x-1
        z=x/y
        pi*=z
    return pi
print(wallis(100000000))        
