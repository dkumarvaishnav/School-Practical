ch="Y"
while (ch=="Y" or ch=="y"):
    print("Enter 1: lines start with g:")
    print("Enter 2: count lines end with a:")
    opt=int(input("Enter your choice:"))
    if opt==1:
        file=open("abc.txt","r")
        line=file.readline()
        while line:
            if line[0]=="g":
                print(line)
            line=file.readline()
        file.close()
    elif opt==2:
        count=0
        f=open("abc.txt","r")
        data=f.readlines()
        for line in data:
            l=len(line)
            if line[l-2]=="a":
                print(line)
                count=count+1
        print("Number of lines having 'a' as last character is/are: ", count)
        f.close()
    else:
        print("invalid Choice")
    ch=(input("Want to continue?"))