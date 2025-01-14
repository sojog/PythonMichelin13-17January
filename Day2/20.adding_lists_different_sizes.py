list_a = [1,2,3,4,5,6,7,8]
list_b = [4,5,6,7]

result_list = []

for i in range(len(list_b)):
    result_list.append(list_a[i] + list_b[i])

print(result_list)


slice_of_list_a =  list_a[len(list_b):]
print(slice_of_list_a)


## V1 - adding elements
result_list += slice_of_list_a

## V2 - extend
result_list.extend(slice_of_list_a)

print(result_list)