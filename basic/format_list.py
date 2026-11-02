string_to_process = "eggs,cheese,milk,bread,cereal"


items = [item.strip().upper() for item in string_to_process.split(",")]

result = " | ".join(items)

print(result)
# Expected Output: "EGGS | CHEESE | MILK | BREAD | CEREAL"