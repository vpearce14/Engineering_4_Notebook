#Quadratic Solver
#Written by Vincent

print("quadratic solver")
print("this will solve for ax^2 + bx + c = 0")

def quad(a, b, c):
    disc = (b*b)-(4*a*c)
    if disc < 0:
        print("there are no real roots")
        return [0]
    if disc >= 0:
        r1 = (-b+(disc**0.5))/(2*a)
        r2 = (-b-(disc**0.5))/(2*a)
        return [r1, r2]

a = int(input('enter the first coefficient'))
b = int(input('enter the second coefficient'))
c = int(input('enter the third coefficient'))

array [quad(a,b,c)]

if len(array) > 1:
    print (array[0], "and", array[1])
