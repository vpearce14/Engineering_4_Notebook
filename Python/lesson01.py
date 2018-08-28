# Calculator
# Written by Vincent
a = int(input('enter a number'))
b = int(input('enter another one'))
def Math(a,b,x):
    if x == 1:
        return a + b
    if x == 2:
        return a - b
    if x == 3:
        return a * b
    if x == 4:
        return a / b
    if x == 5:
        return a % b
print("Sum:\t\t", Math(a,b,1))
print("Difference:\t", Math(a,b,2))
print("Product:\t", Math(a,b,3))
print("Quotient:\t", Math(a,b,4))
print("Modulo:\t\t", Math(a,b,5))
