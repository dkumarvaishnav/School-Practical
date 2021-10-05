def lsearch(ar,n,item):
    for i in range(0,n):
        if ar[i]==item:
            return i
    return -1

n=int(input('enter size of list:'))
print('enter numbers in sorted order:\n')
ar=[0]*n
for i in range(n):
    ar[i]=int(input('Enter the element '))
item=int(input('enter no. to be searched:'))
index=lsearch(ar,n,item)
if index!=-1:
    print('\n element found at index :',index,',position: ',(index+1))
else:
    print('\n sorry, the given number is not found')