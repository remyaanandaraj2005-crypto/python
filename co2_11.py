area_square = lambda side : side * side
area_rectangle = lambda length,width : length * width
area_triangle = lambda s,a,b,c : (s*(s-a)*(s-b)*(s-c)) ** 0.5

a=int(input("Enter the a:"))
b=int(input("Enter the b:"))
c=int(input("Enter the c:"))
s = (a + b + c) / 2

print(area_square(a))
print(area_rectangle(a,b))
print(area_triangle(s,a,b,c))

x = lambda b:b+3
print(x(3))


