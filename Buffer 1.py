def employee(name):
    return name

def salary (exp):
    if exp>=5:
        return 3000000
    elif exp>=3:
        return 1000000
    else:
        return 500000
name = str(input("what is your name: "))
exp = int(input("How long have you been working for? "))
print("The salary of "+str(employee(name))+" is "+str(salary(exp)))