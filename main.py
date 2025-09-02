print("Welcome to the Spectacular... Wonderful... Amazing... Temperature converter.")

def c_to_f(c):
    conv_temp = (c * 1.8) + 32
    print(f'{c}°C is {conv_temp}°F')
    
def f_to_c(f):
    conv_temp = (f - 32) * 0.5555
    print(f'{f}°F is {conv_temp}°C')

def c_to_k(c):
    conv_temp = c + 273.15
    print(f'{c}°C is {conv_temp}°K')

def f_to_k(f):
    conv_temp = (f - 32) * 0.5555 + 273.15
    print(f'{f}°F is {conv_temp}°K')

def k_to_c(k):
    conv_temp = k - 273.15
    print(f'{k}°K is {conv_temp}°C')

def k_to_f(k):
    conv_temp = (k - 273.15) * 1.8 + 32
    print(f'{k}°K is {conv_temp}°F')

def convert():
    while True:
        try:
            convert_choice = int(input("What would you like to convert? \n1. Convert Celsius to Fahrenheit. \n2. Convert Fahrenheit to Celsius.\n3. Convert Celsius to Kelvin. \n4. Convert Fahrenheit to Kelvin. \n5. Convert Kelvin to Celsius. \n6. Convert Kelvin to Fahrenheit. \nPlease pick a number: "))
            break
        except ValueError:
            print("Choice should be a number")

    while True:
        try:
            temp = float(input("Please input the temperature you want to convert: "))
            break
        except ValueError:
            print("Temperature must be a number.")
    
    if convert_choice == 1:
        c_to_f(temp)
    elif convert_choice == 2:
        f_to_c(temp)
    elif convert_choice == 3:
        c_to_k(temp)
    elif convert_choice == 4:
        f_to_k(temp)
    elif convert_choice == 5:
        k_to_c(temp)
    elif convert_choice == 6:
        k_to_f(temp)

while True:
    convert()
    conti = input("Would you like to make another conversion y/n? ")
    if conti == "n":
        break