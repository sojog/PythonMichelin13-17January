"""Create a program that takes two numbers from the user, adds them together, and displays the result."""


while True:
    n1 = input("Insert the first number \n n1=")
    n2 = input("Insert the second number \n n2=")

    n1 = int(n1)
    n2 = int(n2)

    add = n1 + n2
    print("The result is =", add)