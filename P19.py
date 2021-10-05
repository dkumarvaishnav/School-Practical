stk=[]
while True:
    print("Enter 1 : Push")
    print("Enter 2 : Pop")
    print("Enter 3 : Display Stack")
    print("Enter 4 : Exit")
    opt=int(input('enter ur choice:='))
    if opt==1:
        d=(input("enter book name : "))
        stk.append(d)
    elif opt==2:
        if (stk==[]):
            print( "Stack empty")
        else:
            p=stk.pop()
            print ("Deleted element:", p)
    elif opt==3:
        if (stk==[]):
            print( "Stack empty")
        else:
            print ("The stack content is :")
            print(stk)
    elif opt==4:
        break
    else:
        print('invalid choice')
