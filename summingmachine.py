def summing_machine():
    sum = 0
    while True:
        num = input("Enter a number (or 's' to stop): ")
        if num == 's':
            break
        sum += int(num)
    return sum

# Demonstrate the use of the function
result = summing_machine()
print(f"The sum of the numbers entered is: {result}")
