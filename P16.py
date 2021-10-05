import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root",
passwd="Smic123@", database="school")
mycursor=mydb.cursor()
roll=int(input("Enter the roll number of the student to be deleted : "))
rl=(roll,)
mycursor.execute("select * from student")
res=mycursor.fetchall()
print("The Students details before deletion are as follows : ")
print("(ROll, Name, Age, Class, City)")
for x in res:
    print(x)
sql="delete from Student where roll=%s"
mycursor.execute(sql,rl)
print('Record deleted!!!')
mydb.commit()
mycursor.execute("select * from student")
res=mycursor.fetchall()
print("The Students details after deletion are as follows : ")
print("(ROll, Name, Age, Class, City)")
for x in res:
    print(x)
mydb.close()