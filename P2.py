ch = 'Y'
while (ch == 'Y' or ch == 'y'):
    print("Enter 1 : String palindrome:")
    print("Enter 2 : prime no:")
    opt = int(input('enter ur choice:='))
    if opt == 1:
        str = input('Enter Text:=')
        rev = str[::-1]
        if str == rev:
            print(str, "is Palindrome")
        else:
            print(str, "is not Palindrome")
    elif opt == 2:
        no = int(input('Enter Number : '))
        for i in range(2, no):
            ans = no % i
            if ans == 0:
                print("The given number is not a Prime Number")
                break
        else:  # Loop else
            print("The given number is a Prime Number")
    else:
        print('invalid choice')
    ch = (input('want to continue? Y/N'))
