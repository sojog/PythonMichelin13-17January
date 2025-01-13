"""In the program there are two variables that represent the coefficients of the conversion of a currency
	1 eur = 4.97 ron
	1 usd = 4.87 ron
     1 HUF = 0.012 ron
     1 PLN = 1.16 ron

Change the program so that after entering the amount on the user's side, the amount in euros and dollars that the user will receive is displayed."""

EUR = 4.97 
USD = 4.87 
HUF = 0.012 
PLN = 1.16 

amount = int(input("Please insert your amount in RON\n"))
currency = input("Please insert the currency you what to convert to: (EUR, USD, HUF, PLN)\n")

print(currency)
if currency == "EUR":
    print("Suma in EUR = ", amount / EUR)
elif currency == "USD":
    print("Suma in USD = ", amount / USD)
elif currency == "HUF":
    print("Suma in HUF = ", amount / HUF)
elif currency == "PLN":
    print("Suma in PLN = ", amount / PLN)

