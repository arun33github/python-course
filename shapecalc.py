import shapecal

print("welcome to shape calculator : ")
print("enter your choice : ")
print("""1.square\n2.rectangle\n3.triangle\n4.circle\n5.sphere   """)
print("1,2,3,4,5")
print("enter yout choice: ")
choice=input()

if choice=="1":
    side=int(input("area of square :"))
    print("area of square is "+str(shapecal.square(side)))

elif choice=="2":
    len=int(input("enter a length :"))
    bre=int(input("enter a breadth:"))
    print("area of rectangle is "+str(shapecal.rectangle(len,bre)))


elif choice=="3":
    hei=int(input("triangle height :"))
    brea=int(input("triangle breadth:"))
    print("area of triangle is "+str(shapecal.triangle(hei,brea)))

elif choice=="4":
     radius=int(input("enter a radius :"))
     print("radius of a circle is "+str(shapecal.circle(radius)))

elif choice=="5":
    volume=int(input("enter a volume :"))
    print("volume of sphere is "+str(shapecal.sphere(volume)))

else:
    print("invalid choice ")