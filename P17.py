import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root",
passwd="Smic123@", database="school")
mycursor=mydb.cursor()
s=int(input("Enter roll no to search: "))
rl=(s,)
sql="select * from student where roll=%s"
mycursor.execute(sql,rl)
res=mycursor.fetchall()
if not res :
    print("The Given Roll no is not found : ")
else:
    print("The Students details are as follows : ")
    print("(ROll, Name, Age, Class, City)")
    for x in res:
        print(x)
mydb.close()