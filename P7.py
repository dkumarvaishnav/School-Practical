def sumseries(x):
    fact=1
    sum=0
    for i in range(1,7):
        fact=fact*i
        if i%2==0:
            sum=sum-(x**i)/fact
        else:
            sum=sum+(x**i)/fact
    print("Sum  of the given series=",sum)

x=int(input("Enter a term:"))
sumseries(x)