# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  # Conversion factor from Fahrenheit to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # Conversion factor from Celsius to Fahrenheit

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    global FAHRENHEIT_TO_CELSIUS_FACTOR  # Use the global variable
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    global CELSIUS_TO_FAHRENHEIT_FACTOR  # Use the global variable
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    """Main function for temperature conversion."""
    try:
        # Get the temperature value from the user
        temperature = float(input("Enter the temperature to convert: "))
        
        # Get the temperature unit from the user
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "F":
            # Convert from Fahrenheit to Celsius
            celsius = convert_to_celsius(temperature)
            print(f"{temperature} degrees Fahrenheit is {celsius:.2f} degrees Celsius.")
        elif unit == "C":
            # Convert from Celsius to Fahrenheit
            fahrenheit = convert_to_fahrenheit(temperature)
            print(f"{temperature} degrees Celsius is {fahrenheit:.2f} degrees Fahrenheit.")
        else:
            # Handle invalid unit input
            print("Invalid unit! Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        # Handle invalid temperature input
        print("Invalid input! Please enter a numeric value for temperature.")

if __name__ == "__main__":
    main()
