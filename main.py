from swap import swap_numbers_to_strings
from extras.desc import descending_order

def main():
    try:
        num1 = int(input("Enter first number (0 to 3): "))
        num2 = int(input("Enter second number (0 to 3): "))
        
        num1_str, num2_str = swap_numbers_to_strings(num1, num2)
        
        print(f"The two numbers swaped to strings are: {num1_str} and {num2_str}")
    except ValueError:
        print(f"Both numbers need to be in the range from 0 to 3! {ValueError}")
    except Exception:
        print(f"An unexpected error occurred: {Exception}")
        
    try:
        num = int(input("Enter a number to print it in natural descending order: "))
        descending_order(num)
    except ValueError:
        print(f"Enter a non-negative number! {ValueError}")
    except Exception:
        print(f"An unexpected error occurred: {Exception}")
        
if __name__ == "__main__":
    main()