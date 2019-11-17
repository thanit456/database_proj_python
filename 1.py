import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='TestDB',
                                         user='root',
                                         password='password')

    sql_select_Query = "select * from test"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in test is: ", cursor.rowcount)

    print("\nPrinting each test record")
    for row in records:
        print("Id = ", row[0], )
        print("Name = ", row[1])


except Error as e:
    print("Error reading data from MySQL table", e)

finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")
