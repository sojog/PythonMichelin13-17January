EUR = 4.97 
USD = 4.87 
HUF = 0.012 
PLN = 1.16 

amount = 100


should_continue = True

while should_continue:
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
        
    else:
        continue

    answer = input("Do you want to continue? (yes/no)")
    if answer == "no":
        should_continue = False

