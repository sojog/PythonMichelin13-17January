
numbers =  [3, 7, 1, 9, 2, 4, 5, 12]

odd = []
even = []

for i in numbers:
    if i % 2 == 0 :
        even.append(i)
    else:
        odd.append(i)

print("Odd numbers:", odd)
print("Even numbers:", even)
