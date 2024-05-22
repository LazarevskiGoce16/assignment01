def swap_numbers_to_strings(num1, num2):
    num_strings = ["zero", "one", "two", "three"]
    
    if num1 in range(0, 4) and num2 in range(0, 4):
        return num_strings[num1], num_strings[num2]
    else:
        raise ValueError("Both numbers must be in range from 0 to 3!")
