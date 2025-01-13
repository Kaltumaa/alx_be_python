FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR  # Using the global conversion factor
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR  # Using the global conversion factor
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
            print(f"{temperature} degrees Fahrenheit is {celsius:.2f} degrees Celsius.")
        elif unit == "C":
            # Convert from Celsius to Fahrenheit
            fahrenheit = convert_to_fahrenheit(temperature)
            print(f"{temperature} degrees Celsius is {fahrenheit:.2f} degrees Fahrenheit.")
        else:
            print("Invalid unit! Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid input! Please enter a numeric value for temperature.")

if __name__ == "__main__":
    main()
