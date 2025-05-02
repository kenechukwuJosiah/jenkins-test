import sys

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def main():
    print("Welcome to the Jenkins Pipeline Python script!")

    if len(sys.argv) != 2:
        print("Usage: python3 helloworld.py <non-negative-integer>")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
        if number < 0:
            print("Error: Factorial is not defined for negative numbers.")
            sys.exit(1)
        result = factorial(number)
        print(f"The factorial of {number} is {result}.")
    except ValueError:
        print("Invalid input. Please enter a non-negative integer.")
        sys.exit(1)

if __name__ == "__main__":
    main()

