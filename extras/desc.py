def descending_order(num):
    if num < 0:
        raise ValueError("The number must be a non-negative number!")
    while num >= 0:
        print(num, end=" ")
        num -= 1
    print()
