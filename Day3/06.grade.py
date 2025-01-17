
grades = {
    1 : "Insufficient",
    2 : "Sufficient",
    3 : "Average",
    4 : "Good",
    5 : "Excellent"
}

value = int(input("Insert your grade\n"))


# # Version 1
# is_key_found = False
# for key in grades:
#     if key == value:
#         print(grades[value])
#         is_key_found = True
# if not is_key_found:
#     print("Key not found")


# # Version 2
# for key in grades:
#     if key == value:
#         print(grades[value])
#         break
# else:
#     print("Key not found")


# Version 3
if value in grades:
    print(grades[value])
else:
    print("Key not found")


# Version 4
#print(grades.get(value)) # This returns None in case we don't find the value
print(grades.get(value, "Key not found")) # This returns "Key not found" in case we don't find the value