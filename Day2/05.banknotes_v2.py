

initial_amount = int(input("Insert your value"))

amount = initial_amount

tens = amount // 10
print("Banknotes of ten", tens)

amount = amount % 10
fives = amount // 5

print("Banknotes of five", fives)


amount = amount % 5
twos = amount // 2

print("Banknotes of two", twos)


amount = amount % 2
ones = amount // 1

print("Banknotes of one", ones)

print("Initial amount", initial_amount)