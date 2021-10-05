def WRITEMEMBER():
    import pickle
    member={ }
    memfile=open('member.dat','wb')
    ans='y'
    while ans=='y' or ans=='Y':
        mno=int(input('Enter the Member Number'))
        mname=input('Enter the Member Name')
        member['MemberNo']=mno
        member['Name']=mname
        pickle.dump(member,memfile)
        ans=input('Do you want to enter more records (Y/N)….')
    memfile.close()

def DISPLAYSTAFF():
    import pickle
    member={}
    memfile=open('member.dat','rb')
    found=False
    try:
        print('The details of members with Member No. 1005')
        while True:
            member=pickle.load(memfile)
            if member['MemberNo']==1005:
                print(member)
                found=True
    except EOFError:
        if found== False:
            print('No such records found')
        else:
            print('Search Successful')
        memfile.close()

WRITEMEMBER()
DISPLAYSTAFF()