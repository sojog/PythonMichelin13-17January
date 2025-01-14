

start_date = 2001
stop_date = 2025


## Version 1
print("*" * 5 + " Allowed years " + "*" * 5)
for year in range(start_date, stop_date + 1):
    if year % 4 == 0:
        print(year)

print("*" * 5 + len(" Allowed years ") * "*" + "*" * 5)

print()

## Version 2
print("*" * 5 + " Allowed years " + "*" * 5)
if start_date % 4 == 0:
    first_leap_year = start_date
else:
    first_leap_year = start_date // 4 * 4 + 4

# 2001 -> 2004
# 2002 -> 2004
# 2003 -> 2004
# 2004 -> 2004

for year in range(first_leap_year, stop_date + 1, 4):
    print(year)

print("*" * 5 + len(" Allowed years ") * "*" + "*" * 5)