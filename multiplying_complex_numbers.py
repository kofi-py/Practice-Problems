#!"C:\Python310\python.exe"

def multiply_complex_numbers(a=int, b=int, c=int, d=int):
    """Given a, b, c, and d. Returns the the result of the multiplication."""
    real_component = a*c - b*d
    imaginary_component = a*d + b*c
    return "Result: {} + {}i".format(real_component, imaginary_component)


print("Multiplying complex numbers!")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(input("Enter d: "))

output = multiply_complex_numbers(a, b, c, d)
print(output)