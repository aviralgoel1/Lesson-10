def cube(number):
    return number**3

def div_3(number):
    if number %3 == 0:
        return cube(number)
    else:
        return False


print (div_3(10))
print (div_3(12))