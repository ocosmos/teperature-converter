def celsius_kelvin():
    print ('CELSIUS - KELVIN')    
    celsius = float(input("ENTER TEMPERATURE: "))
    kelvin = celsius + 273.15
    print("{} ºCELSIUS = {:.2f} ºKELVIN".format(celsius, kelvin))

def celsius_fahrenheit():
    print ('CELSIUS - FAHRENHEIT')
    celsius = float(input("ENTER TEMPERATURE: "))
    fahrenheit = ((9 * celsius) / 5) + 32
    print("{} ºCELSIUS = {:.2f} ºFAHRENHEIT".format(celsius, fahrenheit))

def celsius_reaumur():
    print ('CELSIUS - RÉAUMUR')
    celsius = float(input("ENTER TEMPERATURE: "))
    reaumur = celsius * 4/5
    print("{} ºCELSIUS = {:.2f} ºRÉAUMUR".format(celsius, reaumur))

def kelvin_celsius():
    print ('KELVIN - CELSIUS')
    kelvin = float(input("ENTER TEMPERATURE: "))
    celsius = kelvin - 273.15
    print("{} ºKELVIN = {:.2f} ºCELSIUS".format(kelvin, celsius))

def kelvin_fahrenheit():
    print ('KELVIN - FAHRENHEIT')
    kelvin = float(input("ENTER TEMPERATURE: "))
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    print("{} ºKELVIN = {:.2f} ºFAHRENHEIT".format(kelvin, fahrenheit))

def kelvin_reaumur():
    print ('KELVIN - RÉAUMUR')
    kelvin = float(input("ENTER TEMPERATURE: "))
    reaumur = (kelvin - 273.15) * 0.8
    print("{} ºKELVIN = {:.2f} ºRÉAUMUR".format(kelvin, reaumur))

def fahrenheit_celsius():
    print ('FAHRENHEIT - CELSIUS')
    fahrenheit = float(input("ENTER TEMPERATURE: "))
    celsius = (fahrenheit - 32) * 5/9
    print("{} ºFAHRENHEIT = {:.2f} ºCELSIUS".format(fahrenheit, celsius))

def fahrenheit_kelvin():
    print ('FAHRENHEIT - KELVIN')
    fahrenheit = float(input("ENTER TEMPERATURE: "))
    kelvin = (fahrenheit - 32) * 5/9 + 273.15
    print("{} ºFAHRENHEIT = {:.2f} ºKELVIN!".format(fahrenheit, kelvin))

def fahrenheit_reaumur():
    print ('FAHRENHEIT - RÉAUMUR')
    fahrenheit = float(input("ENTER TEMPERATURE: "))
    reaumur = (fahrenheit - 32) * 4/9
    print("{} ºFAHRENHEIT = {:.2f} ºRÉAUMUR".format(fahrenheit, reaumur))

def reaumur_celsius():
    print ('RÉAUMUR - CELSIUS')
    reaumur = float(input("ENTER TEMPERATURE: "))
    celsius = reaumur * 5/4
    print("{} ºRÉAUMUR = {:.2f} ºCELSIUS".format(reaumur, celsius))

def reaumur_kelvin():
    print ('RÉAUMUR - KELVIN')
    reaumur = float(input("ENTER TEMPERATURE: "))
    kelvin = reaumur * 5/4 + 273.15
    print("{} ºRÉAUMUR = {:.2f} ºKELVIN!".format(reaumur, kelvin))

def reaumur_fahrenheit():
    print ('RÉAUMUR - FAHRENHEIT')
    reaumur = float(input("ENTER TEMPERATURE: "))
    fahrenheit = reaumur * 9/4 + 32
    print("{} ºRÉAUMUR = {:.2f} ºFAHRENHEIT".format(reaumur, fahrenheit))