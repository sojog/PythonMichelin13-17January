import time

start_time = time.time()

list_a = [1,2,3,4]
list_b = [4,5,6,7,5,6,7,8]

result_list = []

min_len = min(len(list_a), len(list_b))

for i in range(min_len):
    result_list.append(list_a[i] + list_b[i])

result_list += list_a[len(list_b):]
result_list += list_b[len(list_a):]

print(result_list)

stop_time = time.time()
print(f"Executed in {stop_time - start_time}")