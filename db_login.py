import mysql.connector
from mysql.connector import Error

databaseName = 'joo'
tableName = 'accountdetail'
password = 'boss1234'

class Login() :
    def __init__(self, data) :
        self.loginDataObj = LoginDB(data)
    def login(self) :
        return self.loginDataObj.CheckMember(databaseName, tableName)

class LoginDB() :
    def __init__(self,data):
        self.data = data
        self.columns = []
        self.records = []
    def CheckMember(self, databasename, table) :
        wkey = str(self.data[0])
        wpass = str(self.data[1])

        try:
            connection = mysql.connector.connect(host='localhost',database=databaseName,user='root',password='boss1234')
            objdata = (wkey,)
            sqlQuery = "select * from "+table+" where Username = %s"
            
            cursor = connection.cursor()
            cursor.execute(sqlQuery, objdata)
            records = cursor.fetchone()
            self.data = records
                    
        except:
            retmsg = ["1", "Error"]
            print(E)
        else :
            retmsg = ["1", "Username Not Found"]
            if records[1] == wpass :
                retmsg = ["0", "Correct Password"]
            else :
                retmsg = ["1", "Incorrect Password"]
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg
    

