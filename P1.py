ch='Y'
while (ch=='Y' or ch=='y'):
    print("Enter 1 : fibonacci series:")
    print("Enter 2 : factorial:")
    opt=int(input('enter ur choice:='))
    if opt==1:
        n=int(input('enter no. of terms:'))
        no1=0
        no2=1
        x=0
        print("The first ",n, "terms of the fibonacci series is:")
        print(no1,no2,end=" ")
        while(x<=(n-2)):
            no3=no1+no2
            no1=no2
            no2=no3
            print (no3,end=" ")
            x=x+1
    elif opt==2:
        f=1
        n=int(input('enter no:'))
        for i in range(1,n+1):
            f=f*i
        print('factorial is:',f)
    else:
        print('invalid choice')
    ch=(input('want to continue?'))