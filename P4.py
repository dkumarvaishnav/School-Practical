num = input("enter your phone number = ")
if len(num)== 12 :
    if num[3]== "-" :
        if num[4:7].isdigit():
                if num[ 8 : 13 ].isdigit() :
                    if num [7]== "-":
                        if num[ : 3 ].isdigit() :
                            print("it is vaild number ")
                        else :
                            print("it is not vaild number ")
                    else :
                        print("it is not vaild number ")
                else :
                    print("it is not vaild number ")
        else :
            print("it is not vaild number ")
    else :
        print("it is not vaild number ")
else :
    print("it is not vaild number ")
    