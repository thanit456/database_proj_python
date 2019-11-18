import mysql.connector
try:
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="093128156",
    database="testdb"
    )

    print('eiei')
    mycursor = mydb.cursor()

    # mycursor.execute("SELECT * FROM test")
    mycursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS  \
                    WHERE TABLE_NAME = 'test' \
                    ORDER BY ORDINAL_POSITION")

    
  


    myresult = mycursor.fetchall()
    print(myresult)
except:
    print('fail')