from MyPackages.Basic_operations import Arithmetic
from MyPackages.Geometry import Area

print("Arithmetic Operations:")
print("5+3=",Arithmetic.add(5,3))
print("10-7=",Arithmetic.subtract(10,7))
print("5*3=",Arithmetic.multiply(5,3))
print("8/2=",Arithmetic.devide(8,2))
print("8/0=",Arithmetic.devide(8,0))

print("\n Area Cal;culation:")
print("Rectangle (length=5,width=3):",Area.rectangle_area(5,3))
print("Circle (radius=7):",Area.circle_area(7))
print("Triangle (base=4,height=5):",Area.triangle_area(4,5))
