def ser(a,b):
    d=int((b-a)/3)
    print("Series=",a,a+d,a+2*d,b)

first=int(input("Enter first term="))
second=int(input("Enter last term="))

ser(first,second)
