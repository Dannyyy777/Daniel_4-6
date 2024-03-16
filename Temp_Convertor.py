# Name = Daniel Dsouza
# Batch = 4pm - 6pm
# Course = Python
# Topic = Temperature Convertor
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Enter temperature in Celsius = "))

# Function Call -> celsius_to_fahrenheit()
fahrenheit = celsius_to_fahrenheit(celsius)

print("Temperature in Fahrenheit = ", fahrenheit)
