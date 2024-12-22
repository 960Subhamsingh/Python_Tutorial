# Write a program to create area calculation

print("******* Calculater *********8")
print(""" press 1 to get the area of square 
      press 2 to get the area of rectangle 
      press 3 to get the area of circle 
      press 4 to get area of triangle """)

choose= int(input("Enter a number  between 1-4: "))

if(choose==1):
    side = float(input("Enter the lenth of one side: "))
    area = side**2
    print("The area of  square is" , area)

elif(choose==2):
    length = float(input("Enter the length of the rectangle :"))
    width = float(input("Enter the width of the rectangle : "))
    area = length* width
    print("the area of rectangle is " , area)

elif(choose==3):
    radius = float(input("Enter the radius of circle : "))
    area = ((22/7)*(radius**2))
    print("the area of the circle is ", area)

elif(choose==4):
    base = float(input("Enter the base of rectangle : "))
    height = float(input("Enter the height of the triangle: "))
    area_react = 0.5*base*height
    print("Area of the rectangle is  " , area_react)

else:
    print("Invalid input")