def corn():
    a = 7823    #Since variable a is created inside the function corn
    print(a)    #only corn can use the variable a

def fudge():
    print(a)

corn()
fudge()