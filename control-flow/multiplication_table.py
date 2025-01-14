def main():
    """Generates and prints the multiplication table for a given number."""
    try:
        # Prompt the user for a number
        number = int(input("Enter a number to see its multiplication table: "))
        
        # Print the multiplication table using a for loop
        for i in range(1, 11):
            product = number * i
            print(f"{number} * {i} = {product}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
