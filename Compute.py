import sys

# Read the threshold and limit values from the command line arguments
threshold = float(sys.argv[1])
limit = float(sys.argv[2])

# Initialize the cumulative sum to zero
cumulative_sum = 0.0

# Loop over each line of input from standard input
for line in sys.stdin:
    # Parse the input value as a float and strip any whitespace
    input_val = float(line.strip())

    # Subtract the threshold value from the input value if it's greater than the threshold
    if input_val > threshold:
        output_val = input_val - threshold
    else:
        output_val = 0.0

    # If adding the output value to the cumulative sum doesn't exceed the limit, add it
    if input_val + cumulative_sum <= limit:
        cumulative_sum += output_val
        print(output_val)
    else:
        # If adding the output value would exceed the limit, add only the remaining limit
        remaining_limit = limit - cumulative_sum
        if remaining_limit > 0:
            output_val = min(output_val, remaining_limit)
            cumulative_sum += output_val
            print(output_val)
        # Stop processing input values once the limit is reached
        break

# Print the final cumulative sum
print(cumulative_sum)

