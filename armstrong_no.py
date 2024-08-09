# Assign a number to check if it is an Armstrong number
number = 371

# Copy the original number to a new variable
num = number

# Initialize digit and sum variables to 0
digit, sum = 0, 0

# Find the length of the number (i.e., the number of digits)
length = len(str(num))

# Loop through each digit of the number
for i in range(length):
    # Extract the last digit of the number
    digit = int(num % 10)
    
    # Remove the last digit from the number
    num = num / 10
    
    # Add the digit raised to the power of the number's length to the sum
    sum += pow(digit, length)

# Check if the sum of the digits raised to the power of the length equals the original number
if sum == number:
    print("Armstrong")  # If true, the number is an Armstrong number
else:
    print("Not Armstrong")  # If false, the number is not an Armstrong number
