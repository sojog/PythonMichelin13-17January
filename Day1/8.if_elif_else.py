

age = 97

# Version 1
if age < 18:
    print("minor")
else:
    if age < 30:
        print("young adult")
    else:
        if age < 50:
            print("mature")
        else:
            if age < 80:
                print("wise")
            else:
                print("legacy")




# Version 2
if age < 18:
    print("minor")
elif age < 30:
    print("young adult")
elif age < 50:
    print("mature")
elif age < 80:
    print("wise")
else:
    print("legacy") 