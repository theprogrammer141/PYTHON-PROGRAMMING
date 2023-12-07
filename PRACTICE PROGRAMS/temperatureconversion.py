def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def print_temperature_table():
    print("CELSIUS\t\tFAHRENHEIT")
    print("-------------------------")

    for celsius in range(0,101,10):
        fahrenheit=celsius_to_fahrenheit(celsius)
        print(f"{celsius}\t\t{fahrenheit:.2f}")

    print("\nFAHRENHEIT\tCELSIUS")
    print("-------------------------")

    for fahrenheit in range(32, 213, 20):
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}\t\t{celsius:.2f}")


print_temperature_table()
