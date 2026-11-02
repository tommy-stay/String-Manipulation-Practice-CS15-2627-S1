string_to_process = "t H e , T a L e :: O f , T w O :: c I t I e S"

words = [w.replace(" ", "").title() for w in string_to_process.replace(",", "|").replace("::", "|").split("|")]

result = " ".join(words)

print(result)
# Expected Output: The Tale Of Two Cities