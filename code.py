#Temparature conversion from Celsius to Fahrenheit and vice versa


unit=input('enter the temparature units (C or F) :').upper()
temp=float(input(f'enter the temparature in {unit}: '))

if unit=='C':
    F=round((9*temp)/5+32,2)
    print(f"Temparature in Fahrenheit is {F}F")
else:
    C=round((temp-32)*(5/9),2)
    print(f"Temparature in Celsius is {C}C")
