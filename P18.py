import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root",
passwd="Smic123@", database="school")
mycursor=mydb.cursor()
s=int(input("Enter roll no to be searched: "))
rl=(s,)
sql="select * from student where roll=%s"
mycursor.execute(sql,rl)
res=mycursor.fetchall()
if not res :
    print("The Given Roll no is not found : ")
else:
    c=input("Enter the new city name : ")
    print("The Students details before modification is as follows : ")
    print("(ROll, Name, Age, Class, City)")
    for x in res:
        print(x)
    r2=(c,s)
    sql="update student set city= %s where roll=%s"
    mycursor.execute(sql,r2)
    mydb.commit()
    print("Record updated successfully!!!! ")
    sql="select * from student where roll=%s"
    mycursor.execute(sql,rl)
    res=mycursor.fetchall()
    print("The Students details after modification is as follows : ")
    print("(ROll, Name, Age, Class, City)")
    for x in res:
        print(x)
    mydb.close()