from MyPackages.Pack_main.rectangle import area as rect_area, perimeter as rect_perimeter
from MyPackages.Pack_main.circle import area as circle_area, perimeter as circle_perimeter

from MyPackages.Pack_main.pack_sub.cuboid import surface_area as cuboid_surface_area, volume as cuboid_volume
from MyPackages.Pack_main.pack_sub.sphere import surface_area as sphere_surface_area, volume as sphere_volume


print("Rectangle Area:", rect_area(5, 3))
print("Rectangle Perimeter:", rect_perimeter(5, 3))

print("Circle Area:", circle_area(7))
print("Circle Perimeter:", circle_perimeter(7))

print("Cuboid Surface Area:", cuboid_surface_area(5, 3, 4))
print("Cuboid Volume:", cuboid_volume(5, 3, 4))

print("Sphere Surface Area:", sphere_surface_area(7))
print("Sphere Volume:", sphere_volume(7))

