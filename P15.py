import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root",
passwd="Smic123@", database="school")
mycursor=mydb.cursor()
ch='Y'
while ch=='Y' or ch=='y':
    roll=int(input("Enter the roll number : "))
    name=input("Enter the Name: ")
    age=int(input("Enter Age of Student : "))
    class1=input("Enter the Class : ")
    city=input("Enter the City of the Student : ")
    stud=(roll,name,age,class1,city)
    sql="insert into student (roll,name,age,class,city) values(%s,%s,%s,%s,%s)"
    mycursor.execute(sql,stud)
    mydb.commit()
    print('One Record added successfully!!!')
    ch=(input('Do you want to continue? Y/N'))
mycursor.execute("select * from student")
res=mycursor.fetchall()
print("The Students details are as follows : ")
print("(ROll, Name, Age, Class, City)")
for x in res:
    print(x)
mydb.close()