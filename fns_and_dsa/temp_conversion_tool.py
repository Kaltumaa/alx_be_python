# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert a temperature from Fahrenheit to Celsius."""
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert a temperature from Celsius to Fahrenheit."""
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    """Main function for temperature conversion."""
    try:
        # User input for temperature
        temperature = float(input("Enter the temperature to convert: "))
        
        # User input for temperature unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "F":
            # Convert from Fahrenheit to Celsius
            celsius = convert_to_celsius(temperature)
            print(f"{temperature}°F is {celsius:.2f}°C")
        elif unit == "C":
            # Convert from Celsius to Fahrenheit
            fahrenheit = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {fahrenheit:.2f}°F")
        else:
            # Invalid unit input
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        # Handle non-numeric temperature input
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
