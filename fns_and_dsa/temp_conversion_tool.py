FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(temp):
    fahrenheit = (temp * FAHRENHEIT_TO_CELSIUS_FACTOR) +32 
    print(str(temp) + "°F " + "is " + str(fahrenheit) + "°C")
    
    

def convert_to_fahrenheit(temp):
    celsius = (temp * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(str(temp)+ "°C " + "is " + str(celsius) + "°F")

    
def temp_conversion():
    temp = int(input("Enter the temperature to convert: "))
    # if temp is not int:
    #     print("Invalid temperature. Please enter a numeric value.”")
        
    temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F):").upper()
    if temp_type == "F":
        convert_to_celsius(temp)
    elif temp_type == "C":
        convert_to_fahrenheit(temp)
    else:
        print("Please enter 'F' or 'C'")
        
    
temp_conversion()    
    
    
    
