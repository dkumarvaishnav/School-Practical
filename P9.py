def min(x,y):
    a=x%10
    b=y%10
    if a<b:
        return x
    else:
        return y

first=int(input("Enter first number: "))
second=int(input("Enter second number: "))
print("Minimum one's digit number= ", min(first, second))