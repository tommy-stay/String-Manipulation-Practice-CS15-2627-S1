string_to_process = "  18,27,35,20  "

numbers = [int(num.strip()) for num in string_to_process.strip().split(",")]

total = sum(numbers)
average = total / len(numbers)

print(f"Total: {total}")
print(f"Average: {average}")

# Expected Output:
# "Total: 100"
# "Average: 25.0"