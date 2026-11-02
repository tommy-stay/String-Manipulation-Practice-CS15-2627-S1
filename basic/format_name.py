string_to_process = "   sMitH, aLeX    "

last, first = [part.strip() for part in string_to_process.title().split(",")]

result = f"{first} {last}"

print(result)
# Expected output: "Alex Smith"