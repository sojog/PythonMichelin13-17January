list_a = [1,2,3,4,5]
list_b = [4,5,6,7,8]


list_c = []

for i in range(len(list_a)):
    print(list_a[i], list_b[i])
    list_c.append(list_a[i] + list_b[i])

print(list_c)