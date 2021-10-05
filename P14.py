import csv
fh=open('items.csv','w')
iwriter=csv.writer(fh)
ans="y"
itemrec=[["Item_Name","Description","Price"]]
print("Enter item details")
while ans=="y":
    iname=input("Enter Item Code :")
    desc=input("Enter description :")
    price=float(input("Enter price :"))
    itemrec.append([iname,desc,price])
    ans=input("Do you want to enter more Items (Y/N)….")
else:
    iwriter.writerows(itemrec)
    print("Records written successfully")
fh.close()
fh=open("items.csv","r",newline='\r\n')
ireader=csv.reader(fh)
for rec in ireader:
    print(rec)
fh.close()