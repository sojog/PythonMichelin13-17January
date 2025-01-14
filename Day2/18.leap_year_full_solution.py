
start_date = 1400
stop_date = 2025

leap_years = []
print("*" * 5 + " Allowed years " + "*" * 5)
for year in range(start_date, stop_date + 1):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print(year)
        leap_years.append(year)

print("*" * 5 + len(" Allowed years ") * "*" + "*" * 5)


print(leap_years)

