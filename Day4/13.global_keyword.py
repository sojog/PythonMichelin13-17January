
#global variable
variable = 10

def func():
    # local variable
    global variable
    print(variable)
    variable += 1


func()

print(variable)
