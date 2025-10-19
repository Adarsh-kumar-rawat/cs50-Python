text = input("Input: ")
vowels = "aeiouAEIOU"
output = "".join(char for char in text if char not in vowels)
print("Output:", output)
