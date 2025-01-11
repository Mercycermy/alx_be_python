FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FREEZING_POINT_CELSIUS = 32

def convert_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius using the global conversion factor.
    """
    return (fahrenheit - FREEZING_POINT_CELSIUS) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit using the global conversion factor.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_CELSIUS

def main():
    """
    Main function to handle user interaction and temperature conversion.
    """
    try:
        # Prompt user for input
        temp = float(input("Enter the temperature to convert: "))
        scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if scale == 'C':
            # Convert Celsius to Fahrenheit
            converted_temp = convert_to_fahrenheit(temp)
            print(f"{temp}°C is equal to {converted_temp:.2f}°F")
        elif scale == 'F':
            # Convert Fahrenheit to Celsius
            converted_temp = convert_to_celsius(temp)
            print(f"{temp}°F is equal to {converted_temp:.2f}°C")
        else:
            print("Invalid scale. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()