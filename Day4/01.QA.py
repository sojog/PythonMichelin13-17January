# %%
a_b_c = 10_000_000
a_b_c, type(a_b_c)

# %%
a_b_c = 10,000,000
a_b_c, type(a_b_c)

# %%
a b c = 1000000

# %%
abc = 1000000

# %%
"""
# Packing and Unpacking
"""

# %%
a,b,c = 10000, 2000, 3000
print(a)

# %%
"""
# Packing
"""

# %%
a = 10,2
print(a, type(a))

# %%
a = 10.2
print(a, type(a))

# %%
"""
# Unpacking
"""

# %%
x, y = (10,2)
print("x=", x)
print("y=", y)

# %%
import math as mathematics

# %%
mathematics.pi

# %%
do = 30


# %%
catch = 10

# %%
10 / 0 

# %%
int("19")

# %%
a = {1, 2, 3}
print(a, type(a))

# %%
a_list = [3,5,4,3,3,4,5,6,6,4,5,]
a_list = list(set(a_list))
print(a_list)

# %%
"""
# Possible but not preffered way of defining a dictionary
"""

# %%
a = dict(x=2)
a

# %%
"""
# Preffered way of defining a dictionary
"""

# %%
a = {'x':2}
a

# %%
johannis = {'cars':2 , 'houses':6}
johannis['carsss'] = 3
print(johannis)

# %%
x = {"Hello" : ""}
print(bool(x))

# %%
x = {"Hello" : ""}
if x:
    print("x is not empty")
else:
    print("x is empty")


# %%
x = {}
if x:
    print("x is not empty")
else:
    print("x is empty")

# %%
x = {[] : "Hello"}
print(bool(x))

# %%
x = {0 : None}
print(bool(x))

# %%
x = {0 : None}
print(x[0])

# %%
x = {None : None}
print(bool(x))

# %%
x = {None : None}
print(x[None])

# %%
x = "Kill two birds with one stone"
print(x[-4:-1])

# %%
x, y, z = 0, 1, 0
if 1 in (x,y,z):
    print('Yes, it does')
else:
    print('No Chance')

# %%
x, y, z = 0, 1, 0
print("x=",x)

# %%
(x, y, z)

# %%
1 in (0, 1, 0)

# %%
def flodiv(a,b):
    return 1- a // b ** 1
result = flodiv(100, 100)
print (result)

# %%
letters = ["l", "a", "v", "a", "g","m","n", "a"]
index = letters.index("a")
print(index)

# %%
letters = ["l", "a", "v", "a", "g","m","n", "a"]
ch = "a"
indexes = [ i for i in range(len(letters)) if letters[i] == ch]
indexes

# %%
