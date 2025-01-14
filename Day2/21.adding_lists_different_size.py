list_a = [1,2,3,4]
list_b = [4,5,6,7,5,6,7,8]

result_list = []

if len(list_a) > len(list_b):
    short_list = list_b
    long_list = list_a
else:
    short_list = list_a
    long_list =list_b


for i in range(len(short_list)):
    result_list.append(list_a[i] + list_b[i])


slice_of_list_a =  long_list[len(short_list):]

result_list += slice_of_list_a

print(result_list)