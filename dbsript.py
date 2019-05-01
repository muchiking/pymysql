#!/usr/bin/python3

import pymysql as PyMySQL


def veiw():
    db = PyMySQL.connect("localhost", "muchi", "password", "books")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM record")
    rows = cursor.fetchall()
    for row in rows:
        # print(row["Author "], row["Price"], row["title "], row["book_no "], row["no_of_copies "])
        print("{0} {1} {2}".format(row[0], row[1], row[2]))


def insert(author, price, title, book_no, no_copies):
    test = (author, price, title, book_no, no_copies)
    db = PyMySQL.connect("localhost", "muchi", "password", "books")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = ("INSERT INTO record(Author ,Price, title, book_no ,no_of_copies) \n"
           "    VALUES (%s, %s, %s, %s, %s)")
    # cursor.execute(sql,test)
    # Commit your changes in the database
    # db.commit()
    # print("succes")
    try:

        # Execute the SQL command
        cursor.execute(sql, test)
        # Commit your changes in the database
        db.commit()
        print("succes")

    except:
        # Rollback in case there is any error
        print("fail")
        db.rollback()

    # disconnect from server
    db.close()


selector = input(print("select action " + " " + "to insert data select insert " + " to view data write view"))
if selector == "insert":
    kip = input(print("enter authers name\n"))
    num = input(print("input book price\n"))
    name = input(print("enter book title\n"))
    number = input(print("enter book number\n"))
    copys = input(print("enter the number of copies\n"))
    insert(kip, num, name, number, copys)

elif selector == "veiw":
    veiw()

else:
    exit()  
