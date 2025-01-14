
initial_amount = int(input("Insert your value"))
amount = initial_amount


# banknotes = [10, 5, 2, 1]

banknotes = [100, 50, 20, 10, 5, 1]

for note in banknotes:
    value = amount // note
    print("Banknotes of", note, ":", value)
    print(f"Banknotes of {note} : {value}")
    amount = amount % note

print("Initial amount", initial_amount)