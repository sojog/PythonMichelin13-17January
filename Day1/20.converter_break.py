EUR = 4.97 
USD = 4.87 
HUF = 0.012 
PLN = 1.16 

amount = 100
currency = input("Please insert the currency you what to convert to: (EUR, USD, HUF, PLN)\n")
currency = currency.upper()

while True:
    if currency == "EUR":
        print("Sum in EUR = ", amount / EUR)
        break
    elif currency == "USD":
        print("Sum in USD = ", amount / USD)
        break
    elif currency == "HUF":
        print("Sum in HUF = ", amount / HUF)
        break
    elif currency == "PLN":
        print("Sum in PLN = ", amount / PLN)
        break
    else:
        currency = input("Please insert the currency you what to convert to: (EUR, USD, HUF, PLN)\n")
        currency = currency.upper()