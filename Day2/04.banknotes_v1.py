

amount = 128

tens = amount // 10
print("Banknotes of ten", tens)

rest_after_10 = amount % 10
fives = rest_after_10 // 5

print("Banknotes of five", fives)


rest_after_5 = rest_after_10 % 5
twos = rest_after_5 // 2

print("Banknotes of two", twos)


rest_after_2 = rest_after_5 % 2
ones = rest_after_2 // 1

print("Banknotes of one", ones)