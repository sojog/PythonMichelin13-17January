
## In python we have first class functions

def my_func():
    print("my_func is called")

my_func()
print(my_func)

x = my_func
x()


to_terminal = print
to_terminal(43, 532, 532, 532, sep="^^")