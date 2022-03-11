# SOURCE CODE

# MODULE : LIBRARY MANAGEMENT

import menulib
import Book
import issue

while True:
    Book.clrscreen()
    print("\t\t\t Library Management\n")
    print("==============================================================")
    print("1. Book Management ")
    print("2. Members Management ")
    print("3. Issue/Return Book ")
    print("4. Exit ")
    print("==============================================================")
    choice = int(input("Enter Choice between 1 to 4-------> : "))
    if choice == 1:
        menulib.MenuBook()
    elif choice == 2:
        menulib.MenuMember()
    elif choice == 3:
        menulib.MenuIssueReturn()
    elif choice == 4:
        break
    else:
        print("Wrong Choice......Enter Your Choice again")
    x = input("Enter any key to continue")

####################################################################################################

# PYTHON MODULE : MENULIB

import Book
import member

import issue


def MenuBook():
    while True:
        Book.clrscreen()
        print("\t\t\t Book Record Management\n")
        print("============================================================")
        print("1. Add Book Record ")
        print("2. Display Book Records ")
        print("3. Search Book Record ")
        print("4. Delete Book Record ")
        print("5. Update Book Record ")
        print("6. Return to Main Menu ")
        print("============================================================")
        choice = int(input("Enter choice between 1 to 5 -------> "))
        if choice == 1:
            Book.insertData()
        elif choice == 2:
            Book.display()
        elif choice == 3:
            Book.SearchBookRec()
        elif choice == 4:
            Book.deleteBook()
        elif choice == 5:
            Book.UpdateBook()
        elif choice == 6:
            return
        else:
            print("Wrong choice... Enter your choice again")
        x = input("Enter any key to continue")


# ----------------------------------------------------------------------------------------

def MenuMember():
    while True:
        Book.clrscreen()
    print("\t\t\t Member Record Management\n")
    print("============================================================")
    print("1. Add Member Record ")
    print("2. Display Member Records ")
    print("3. Search Member Record ")
    print("4. Delete Member Record ")
    print("5. Update Member Record ")
    print("6. Return to Main Menu ")
    print("============================================================")
    choice = int(input("Enter Choice between 1 to 5-------> : "))
    if choice == 1:
        member.insertMember()
    elif choice == 2:
        member.display()
    elif choice == 3:
        member.SearchMember()
    elif choice == 4:
        member.deleteMember()
    elif choice == 5:
        member.UpdateMember()
    elif choice == 6:
        return
    else:
        print("Wrong Choice......Enter Your Choice again")
    x = input("Enter any key to continue")


# ----------------------------------------------------------------------------------------

def MenuIssueReturn():
    while True:
        Book.clrscreen()
        print("\t\t\t Member Record Management\n")
        print("============================================================")
        print("1. Issue Book ")
        print("2. Display Issued Book Records ")
        print("3. Return Issued Book ")
        print("4. Return to Main Menu ")
        print("============================================================")
        choice = int(input("Enter Choice between 1 to 5-------> : "))
        if choice == 1:
            issue.issueBook()
        elif choice == 2:
            issue.ShowIssuedBooks()
        elif choice == 3:
            issue.returnBook()
        elif choice == 4:
            return
        else:
            print("Wrong Choice......Enter Your Choice again")
        x = input("Enter any key to continue")


####################################################################################################

# PYTHON MODULE : BOOK

import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import (connection)
import os
import platform


def clrscreen():
    if platform.system() == "Windows":
        print(os.system("cls"))


def display():
    try:
        os.system('cls')
        cnx = connection.MySQLConnection(user='root',
                                         passwd='Smic123\"', host='localhost', database='LIbrary')
        Cursor = cnx.cursor()
        query = ("SELECT * FROM BookRecord")
        Cursor.execute(query)
        for (Bno, Bname, Author, price, publ, qty, d_o_purchase) in Cursor:
            print("===========================================================")
            print("Book Code : ", Bno)
            print("Book Name : ", Bname)
            print("Author of Book : ", Author)
            print("Price of Book : ", price)
            print("Publisher : ", publ)
            print("Total Quantity in Hand : ", qty)
            print("Purchased On : ", d_o_purchase)
            print("===========================================================")
        Cursor.close()
        cnx.close()
        print("You have done it!!!!!!")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    # else:
    # cnx.close()


def insertData():
    try:
        cnx = connection.MySQLConnection(user='root', passwd='Smic123\"', host='localhost',
                                         database='Library')
        Cursor = cnx.cursor()
        bno = input("Enter Book Code : ")
        bname = input("Enter Book Name : ")
        Auth = input("Enter Book Author's Name : ")
        price = int(input("Enter Book Price : "))
        publ = input("Enter Publisher of Book : ")
        qty = int(input("Enter Quantity purchased : "))
        print("Enter Date of Purchase (Date/MOnth and Year seperately: ")
        DD = int(input("Enter Date : "))
        MM = int(input("Enter Month : "))
        YY = int(input("Enter Year : "))
        Qry = ("INSERT INTO BookRecord VALUES (%s, %s, %s, %s, %s, %s, %s)")
        data = (bno, bname, Auth, price, publ, qty, date(YY, MM, DD))
        Cursor.execute(Qry, data)
        # Make sure data is committed to the database
        cnx.commit()
        Cursor.close()
        cnx.close()
        print("Record Inserted..............")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    # cnx.close()


def deleteBook():
    try:
        cnx = connection.MySQLConnection(user='root', passwd='Smic123\"', host='localhost',
                                         database='Library')
        Cursor = cnx.cursor()
        bno = input("Enter Book Code of Book to be deleted from the Library : ")
        Qry = ("""DELETE FROM BookRecord WHERE BNO = %s""")
        del_rec = (bno,)
        Cursor.execute(Qry, del_rec)
        # Make sure data is committed to the database
        cnx.commit()
        Cursor.close()
        cnx.close()
        print(Cursor.rowcount, "Record(s) Deleted Successfully.............")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        # cnx.close()


def SearchBookRec():
    try:
        cnx = connection.MySQLConnection(user='root', passwd='Smic123\"', host='localhost',
                                         database='Library')
        Cursor = cnx.cursor()
        bno = input("Enter Book No to be Searched from the Library : ")
        query = ("SELECT * FROM BookRecord where BNo = %s ")
        rec_srch = (bno,)
        Cursor.execute(query, rec_srch)
        Rec_count = 0
        for (Bno, Bname, Author, price, publ, qty, d_o_purchase) in Cursor:
            Rec_count += 1
            print("===========================================================")
            print("Book Code : ", Bno)
            print("Book Name : ", Bname)
            print("Author of Book : ", Author)
            print("Price of Book : ", price)
            print("Publisher : ", publ)
            print("Total Quantity in Hand : ", qty)
            print("Purchased On : ", d_o_purchase)
            print("===========================================================")
            if Rec_count % 2 == 0:
                input("Press any key to continue")
                clrscreen()
        print(Rec_count, "Record(s) found")
        # Make sure data is committed to the database
        cnx.commit()
        Cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        # cnx.close()


def UpdateBook():
    try:
        cnx = mysql.connector.connect(host="localhost", user="root", passwd="Smic123\"",
                                      database="library")
        Cursor = cnx.cursor()
        bno = input("Enter Book Code of Book to be Updated from the Library : ")
        # query = ("SELECT * FROM BookRecord where BNo = %s ")
        # rec_srch=(bno,)
        print("Enter new data ")
        bname = input("Enter Book Name : ")
        Auth = input("Enter Book Author's Name : ")
        price = int(input("Enter Book Price : "))
        publ = input("Enter Publisher of Book : ")
        qty = int(input("Enter Quantity purchased : "))
        print("Enter Date of Purchase (Date/MOnth and Year seperately: ")
        DD = int(input("Enter Date : "))
        MM = int(input("Enter Month : "))
        YY = int(input("Enter Year : "))
        Qry = ("UPDATE BookRecord SET bname=%s,Author=%s,price=%s,publisher=%s,qty=%s,d_o_purchase=%s WHERE BNO=%s")
        data = (bname, Auth, price, publ, qty, date(YY, MM, DD), bno)
        Cursor.execute(Qry, data)
        # Make sure data is committed to the database'''
        cnx.commit()
        Cursor.close()
        cnx.close()
        print(Cursor.rowcount, "Record(s) Updated Successfully.............")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        # cnx.close()


####################################################################################################

# PYTHON MODULE : ISSUE

import mysql.connector
from mysql.connector import errorcode
from datetime import date
from mysql.connector import (connection)
import os


def clrscreen():
    print('\n' * 5)


def ShowIssuedBooks():
    try:
        os.system('cls')
        cnx = connection.MySQLConnection(user='root', password='Smic123\"', host='localhost',
                                         database='Library')
        Cursor = cnx.cursor()
        query = (
            "SELECT B.bno,bname,M.mno,mname,d_o_issue,d_o_ret FROM bookRecord B,issue I,member M where B.bno=I.bno and I.mno=M.mno")
        Cursor.execute(query)
        for (Bno, Bname, Mno, Mname, doi, dor) in Cursor:
            print("===========================================================")
            print("Book Code : ", Bno)
            print("Book Name : ", Bname)
            print("Member Code : ", Mno)
            print("Member Name : ", Mname)
            print("Date of issue : ", doi)
            print("Date of return : ", dor)
            print("===========================================================")
        Cursor.close()
        cnx.close()
        print("You have done it!!!!!!")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()


def issueBook():
    try:
        cnx = connection.MySQLConnection(user='root', password='Smic123\"', host='localhost',
                                         database='Library')
        Cursor = cnx.cursor()
        bno = input("Enter Book Code to issue : ")
        mno = input("Enter Member Code : ")
        issueDate = date.today()
        Qry = ("INSERT INTO issue (bno,mno,d_o_issue) VALUES (%s, %s, %s)")
        data = (bno, mno, issueDate)
        Cursor.execute(Qry, data)
        cnx.commit()
        Cursor.close()
        cnx.close()
        print("Record Inserted..............")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    # cnx.close()


def returnBook():
    try:
        cnx = connection.MySQLConnection(user='root', password='Smic123\"', host='localhost',
                                         database='Library')
        Cursor = cnx.cursor()
        bno = input("Enter Book Code of Book to be returned to the Library : ")
        Mno = input("Enter Member Code of Member who is returning Book : ")
        retDate = date.today()
        Qry = ("""Update Issue set d_o_ret= %s WHERE BNO = %s and Mno= %s """)
        rec = (retDate, bno, Mno)
        Cursor.execute(Qry, rec)
        # Make sure data is committed to the database
        cnx.commit()
        Cursor.close()
        cnx.close()
        print(Cursor.rowcount, "Record(s) Deleted Successfully.............")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    # cnx.close()


####################################################################################################

# PYTHON MODULE : MEMBER

import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import (connection)
import os


def clrscreen():
    print('\n' * 5)


def display():
    try:
        os.system('cls')
        cnx = connection.MySQLConnection(user='root', password='Smic123\"', host='localhost',
                                         database='LIbrary')
        Cursor = cnx.cursor()
        query = ("SELECT * FROM Member")
        Cursor.execute(query)
        for (Mno, Mname, MOB, DOP, ADR) in Cursor:
            print("===========================================================")
            print("Member Code : ", Mno)
            print("Member Name : ", Mname)
            print("Mobile No.of Member : ", MOB)
            print("Date of Membership : ", DOP)
            print("Address : ", ADR)
            print("===========================================================")
        Cursor.close()
        cnx.close()
        print("You have done it!!!!!!")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    # else:
    # cnx.close()


def insertMember():
    try:
        cnx = connection.MySQLConnection(user='root', password='Smic123\"', host='localhost',
                                         database='Library')
        Cursor = cnx.cursor()
        mno = input("Enter Member Code : ")
        mname = input("Enter Member Name : ")
        mob = input("Enter Member Mobile No. : ")
        print("Enter Date of Membership (Date/MOnth and Year seperately: ")
        DD = int(input("Enter Date : "))
        MM = int(input("Enter Month : "))
        YY = int(input("Enter Year : "))
        addr = input("Enter Member Adress : ")
        Qry = ("INSERT INTO Member VALUES (%s, %s, %s, %s, %s)")
        data = (mno, mname, mob, date(YY, MM, DD), addr)
        Cursor.execute(Qry, data)
        # Make sure data is committed to the database
        cnx.commit()
        Cursor.close()
        cnx.close()
        print("Record Inserted..............")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    # cnx.close()


def deleteMember():
    try:
        cnx = connection.MySQLConnection(user='root', passwd='Smic123\"', host='localhost',
                                         database='Library')
        Cursor = cnx.cursor()
        mno = input("Enter Member Code to be deleted from the Library : ")
        Qry = ("""DELETE FROM Member WHERE MNO = %s""")
        del_rec = (mno,)
        Cursor.execute(Qry, del_rec)
        # Make sure data is committed to the database
        cnx.commit()
        Cursor.close()
        cnx.close()
        print(Cursor.rowcount, "Record(s) Deleted Successfully.............")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    # cnx.close()


def SearchMember():
    try:
        cnx = connection.MySQLConnection(user='root', password='Smic123\"', host='localhost',
                                         database='Library')
        Cursor = cnx.cursor()
        mnm = input("Enter the Member Code to be Searched : ")
        query = ("SELECT * FROM Member where mno = %s")
        rec_srch = (mnm,)
        Cursor.execute(query, rec_srch)
        Rec_count = 0
        for (Mno, Mname, MOB, DOP, ADR) in Cursor:
            print("===========================================================")
            print("Member Code : ", Mno)
            print("Member Name : ", Mname)
            print("Mobile No.of Member : ", MOB)
            print("Date of Membership : ", DOP)
            print("Address : ", ADR)
            print("===========================================================")
            if Rec_count % 2 == 0:
                input("Press any key to continue")
                clrscreen()
        print(Rec_count, "Record(s) found")
        cnx.commit()
        Cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)


def UpdateMember():
    try:
        cnx = mysql.connector.connect(host="localhost", user="root", passwd="Smic123\"",
                                      database="library")
        Cursor = cnx.cursor()
        mno = input("Enter the Member Code to be Updated : ")
        print("Enter new data ")
        mname = input("Enter Member Name : ")
        mob = input("Enter Member Mobile No. : ")
        print("Enter Date of Membership (Date/MOnth and Year seperately: ")
        DD = int(input("Enter Date : "))
        MM = int(input("Enter Month : "))
        YY = int(input("Enter Year : "))
        addr = input("Enter Member Adress : ")
        Qry = ("UPDATE member SET mname=%s,mob=%s,dop=%s,adr=%s WHERE mno=%s")
        data = (mname, mob, date(YY, MM, DD), addr, mno)
        Cursor.execute(Qry, data)
        cnx.commit()
        Cursor.close()
        cnx.close()
        print(Cursor.rowcount, "Record(s) Updated Successfully.............")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
