
def add(a, b):
    return a + b

def diff(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b


def do_operation(a, b, operation):
    return operation(a, b)


print(do_operation(30, 50, add))
print(do_operation(3, 1, mult))