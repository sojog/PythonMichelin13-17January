# %%
a = 10
b = 20 

# %%
a = 10
b = 20
a = b
b = a

print("a=", a)
print("b=", b)

# %%
a = 10
b = 20
aux = b
b = a
a = aux

print("a=", a)
print("b=", b)

# %%
a = 10
b = 20
a, b = b, a

print("a=", a)
print("b=", b)

# %%
"""
# Number of values to unpacked must be equal to numbers of variables
"""

# %%
a, b = 10, 2, 3

# %%
"""
# Number of values to unpacked must be equal to numbers of variables
"""

# %%
a, b, c, d = 10, 2, 3

# %%
a, *b = 10, 2, 3, 4, 64, 3, 4
print("a=", a)
print("b=", b)

# %%
a, *b, c = 10, 2, 3, 4, 64, 3, 4
print("a=", a)
print("b=", b)
print("c=", c)

# %%
print(1,2,4,5,6,7,7,8,6,4,4,3,3,3,3,3,3,3,4,4,4)

# %%
def func_with_params(*parameters):
    print("parameters:", parameters, type(parameters))


func_with_params()

# %%
def func_with_params(*parameters):
    print("parameters:", parameters, type(parameters))


func_with_params(2,3)

# %%
def func_with_params(*parameters):
    print("parameters:", parameters, type(parameters))


func_with_params(2,3,5,6,5,4,43,324,4,4,43,43,43,243,4,423,4236,464,45,54,534,5,5,534,534,534,534)

# %%
def func_with_params(first, second, *parameters):
    print("first:", first, "second:", second)
    print("parameters:", parameters, type(parameters))


func_with_params(2,3,5,6,5,4,43,)

# %%
def func_with_params(first, second, *parameters):
    print("first:", first, "second:", second)
    print("parameters:", parameters, type(parameters))


func_with_params(2,3,5,6,5,4,43,)

# %%
def func_with_params(anything, polenta, *parameters):
    print("anything:", anything, "polenta:", polenta)
    print("parameters:", parameters, type(parameters))


func_with_params(1, 321)

# %%
def func_with_params(first, second, *args, **kargs):
    print("first:", first, "second:", second)
    print("args:", args, type(args))
    print("kargs:", kargs, type(kargs))


func_with_params(1,2, 32, 4)


# %%
def func_with_params(first, second, *args, **kargs):
    print("first:", first, "second:", second)
    print("args:", args, type(args))
    print("kargs:", kargs, type(kargs))
    print(kargs['generic'])


func_with_params(1,2, 32, 4, generic="hello", dubai=30)

# %%
def func_with_params(first, second, *args, **kargs):
    print("first:", first, "second:", second)
    print("args:", args, type(args))
    print("kargs:", kargs, type(kargs))
    print(kargs['generic'])


func_with_params(1,2, 32, 4, generic="hello", dubai=30)