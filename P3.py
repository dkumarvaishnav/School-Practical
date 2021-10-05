n1=0
while True :
    a = input("enter a number (for quit enter q) = ")
    if a == "q" or a== "Q" :
        break
    else :
        n=int(a)
        while n>0:
            d=n%10
            n1=n1*10+d
            n=n//10
        if int(a) == n1 :
            print(n1,"is palindromes of ", int(a))
        else :
            print(n1,"is not palindromes of ",int(a))
        n1=0