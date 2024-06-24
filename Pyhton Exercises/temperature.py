print("""
Select a Unit:
1 - Fahrenheit 
2 - Celcuis
3 - Kelvin
 """)

unit = str(input("Enter a Unit: "))
temp = int(input("Enter a temperature: "))

if unit == "1":
    if temp >= 212:
        print("Your temperature can boil")
    else:
        print("Your temperature cannot boil")
elif unit == "2":
    if temp >= 100:
        print("Your temperature can boil")
    else:
        print("Your temperature cannot boil")
elif unit == "3":
    if temp >= 373:
        print("Your temperature can boil")
    else:
        print("Your temperature cannot boil")
else:
    print("Invalid Unit")

