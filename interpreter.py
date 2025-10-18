# interpreter.py
expression = input("Enter an arithmetic expression (x y z): ").strip()

# Split the input into three parts: x, operator, z
x_str, operator, z_str = expression.split()

# Convert x and z to integers
x = int(x_str)
z = int(z_str)

# Perform the calculation based on the operator
if operator == "+":
    result = x + z
elif operator == "-":
    result = x - z
elif operator == "*":
    result = x * z
elif operator == "/":
    result = x / z
else:
    raise ValueError("Invalid operator")

print(f"{result:.1f}")
