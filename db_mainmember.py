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
            connection = mysql.connector.connect(host='localhost',database=databaseName,user='root',password=password)
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

class Register():
    def __init__(self, data) :
        self.registerDataObj = RegisterDB(data)
    def register(self) :
        return self.registerDataObj.AddNewMember(databaseName, tableName)

class RegisterDB() :
    def __init__(self,data):
        self.data = data
        self.columns = []
        self.records = []

    def AddNewMember(self, databasename, table) :
        wdata=self.data

        try:
            connection = mysql.connector.connect(host='localhost', database=databasename, user='root', password='boss1234')
       
            objdata1 = (wdata[2], wdata[3])
            objdata2 = (wdata[0], wdata[1])
            table1 = 'member_t'
            
            sqlQuery1 = "insert into "+table+" (Username, Password) " \
                               "values (%s,%s)"
            # sqlQuery3 = "insert into member_t values (%s,%s,'19/11/2562','19/11/2563',0)"
            sqlQuery2 = "insert into "+table1+" (MemberIDNumber, FirstName, LastName, StartDate, ExpireDate, MemberPoints) " \
                                "values ('1234567891011',%s,%s,'2019-11-20','2020-11-20',0)"
            
            cursor = connection.cursor()
            cursor.execute(sqlQuery1, objdata1)
            cursor.execute(sqlQuery2, objdata2)
            
            connection.commit()

        except:
            retmsg = ["1", "Add error"]
        else :
            retmsg = ["0", "Add done"]
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg
    
