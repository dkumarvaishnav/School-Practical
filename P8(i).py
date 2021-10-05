def cube(a=2):
    print("Cube of",a,"=",a**3)
    
num=input("Enter a number (For empty press Enter):")
if num=="":
    cube()
else:
    cube(int(num))
