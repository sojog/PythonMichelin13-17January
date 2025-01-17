# %%
div = 0

try:
    10 / div
    print("The program should continue")
except:
    print("The error occured")

# %%
div = 2

try:
    10 / div
    print("The program should continue")
except:
    print("The error occured")

# %%
div = 2

try:
    10 / div
    print("The program should continue")
except ZeroDivisionError:
    print("The error occured")

# %%
div = "23jhj"

try:
    int(div)
    print("The program should continue")
except ZeroDivisionError:
    print("The error ZeroDivisionError occured")
except ValueError:
    print("The error ValueError occured")

# %%
div = "23jhj"

try:
    div + 30
    print("The program should continue")
except ZeroDivisionError:
    print("The error ZeroDivisionError occured")
except ValueError:
    print("The error ValueError occured")
except:
    print("General exception")

# %%
div = "23jhj"

try:
    div + 30
    print("The program should continue")
except ZeroDivisionError:
    print("The error ZeroDivisionError occured")
except ValueError:
    print("The error ValueError occured")
except:
    print("General exception")
finally:
    print("This line is executed regardless of error occurances")

# %%
div = 100

try:
    div + 30
    print("The program should continue")
except ZeroDivisionError:
    print("The error ZeroDivisionError occured")
except ValueError:
    print("The error ValueError occured")
except:
    print("General exception")
finally:
    print("This line is executed regardless of error occurances")

# %%
