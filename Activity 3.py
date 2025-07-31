def factorial (x):
    '''This is a recursive function to find the factoial of an integer'''

    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)

while True:
    print(factorial.__doc__)
    n=int(input("enter a number: "))

    print(factorial(n))