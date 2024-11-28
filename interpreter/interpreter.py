#using split method for simple arthimethic in python
#submit50 cs50/problems/2022/python/interpreter
x, y, z = input("Expression: ").split(" ")

x=float(x)
z=float(z)

if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    if z != 0:
        result = x / z
    else:
        result = "Error: Division by zero."
else:
    result="Error: Invalid operator."
print("Result:", result)
