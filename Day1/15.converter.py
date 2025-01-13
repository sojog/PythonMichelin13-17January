
EUR = 4.97 
USD = 4.87 
HUF = 0.012 
PLN = 1.16 

# amount = int(input("Please insert your amount in RON\n"))
amount = 100
currency = input("Please insert the currency you what to convert to: (EUR, USD, HUF, PLN)\n")
currency = currency.upper()


while currency != "EUR" and currency != "USD" and currency != "HUF" and currency != "PLN":
    currency = input("Please insert the currency you what to convert to: (EUR, USD, HUF, PLN)\n")
    currency = currency.upper()


if currency == "EUR":
    print("Sum in EUR = ", amount / EUR)
elif currency == "USD":
    print("Sum in USD = ", amount / USD)
elif currency == "HUF":
    print("Sum in HUF = ", amount / HUF)
elif currency == "PLN":
    print("Sum in PLN = ", amount / PLN)

