import mysql.connector
from mysql.connector import Error
try:
    connection = mysql.connector.connect(host='localhost',database='testdb',user='root',password='448800')
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
        cursor.close()
        connection.close()
        print("MySQL connection is closed")