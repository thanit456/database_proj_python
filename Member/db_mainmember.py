import mysql.connector
from mysql.connector import Error

#hyperparameter
databaseName = 'too_superstore'
password = 'boss1234'

class Login() :
    def __init__(self, data) :
        self.loginDataObj = LoginDB(data)
    def login(self) :
        return self.loginDataObj.CheckMember(databaseName)

class LoginDB() :
    def __init__(self,data):
        self.data = data
        self.columns = []
        self.records = []
    def CheckMember(self, databasename) :
        wkey = str(self.data[0])
        wpass = str(self.data[1])

        try:
            connection = mysql.connector.connect(host='localhost',database=databaseName,user='root',password=password)
            objdata = (wkey,)
            sqlQuery = "select * from "+"member_t"+" where Username = %s"
            
            cursor = connection.cursor()
            cursor.execute(sqlQuery, objdata)
            records = cursor.fetchone()
            self.data = records
                    
        except:
            retmsg = ["1", "Error"]
        else :
            retmsg = ["1", "Username Not Found"]
            if records[-1] == wpass :
                retmsg = ["0", "Correct Password",wkey]
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
        return self.registerDataObj.AddNewMember(databaseName)

class RegisterDB() :
    def __init__(self,data):
        self.data = data
        self.columns = []
        self.records = []

    def AddNewMember(self, databasename) :
        wdata=self.data

        try:
            connection = mysql.connector.connect(host='localhost', database=databasename, user='root', password=password)
       
            objdata = (wdata[2],wdata[0],wdata[1], wdata[3],wdata[4])
            sqlQuery = "insert into "+"member_t"+" (MemberIDNumber, FirstName, LastName, StartDate, ExpireDate, MemberPoints, UserName, Password) " \
                                "values (%s,%s,%s,'2019-11-23','2020-11-23',0,%s,%s)"
            
            cursor = connection.cursor()
            cursor.execute(sqlQuery, objdata)
            
            connection.commit()

        except:
            retmsg = ["1", "Add error"]
        else :
            retmsg = ["0", "Add done"]
        finally:
            if (connection.is_connected()):
                connection.close()
            return retmsg
    
class Promotion() :
    def __init__(self, data) :
        self.promotionDataObj = PromotionDB(data)

    def showTable(self):
        return self.promotionDataObj.showTable(databaseName)
    
class PromotionDB() :

    def __init__(self, data) :
        self.data = data
        self.columns = []
        self.records = []
    
    def showTable(self, databasename):
        try:
            connection = mysql.connector.connect(host='localhost', database=databasename, user='root', password=password)
            
            wdata = self.data

            if (wdata[0].strip() == ''):
                sqlQuery = "SELECT promotion.PromotionID as promotionid,promotion.ProductID as productid,product.Name as productname,promotion.StartDate as startdate,promotion.EndDate as enddate,promotion.MemberPointCost as mempoint,product.Price as oldprice,promotion.Percentage as discount,FLOOR(product.Price*(100-promotion.Percentage)/100) as newprice FROM promotion INNER JOIN product ON promotion.ProductID=product.ProductID;"      
            else :
                sqlQuery = "SELECT promotion.PromotionID as promotionid,promotion.ProductID as productid,product.Name as productname,promotion.StartDate as startdate,promotion.EndDate as enddate,promotion.MemberPointCost as mempoint,product.Price as oldprice,promotion.Percentage as discount,FLOOR(product.Price*(100-promotion.Percentage)/100) as newprice FROM promotion INNER JOIN product ON promotion.ProductID=product.ProductID WHERE product.Name="+"'"+str(wdata[0].strip())+"'"+";"
            
            cursor = connection.cursor()
            cursor.execute(sqlQuery)
            self.records = cursor.fetchall()
                   
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return self.records

class SelectMemInfo() :
    def __init__(self, data) :
        self.SelectMemInfoDataObj = SelectMemInfoDB(data)
    def showmeminfo(self) :
        return self.SelectMemInfoDataObj.MemberInfo(databaseName)

class SelectMemInfoDB() :
    def __init__(self,data):
        self.data = data
        self.records = []
    def MemberInfo(self, databasename) :
        wkey = str(self.data[0])

        try:
            connection = mysql.connector.connect(host='localhost',database=databaseName,user='root',password=password)
            objdata = (wkey,)
            sqlQuery = "select * from "+"member_t"+" where Username = %s"
            
            cursor = connection.cursor()
            cursor.execute(sqlQuery, objdata)
            records = cursor.fetchone()
            self.data = records
                    
        except:
            retmsg = ["1", "Error"]
            print(E)
        else :
            retmsg = ["0", " ShowInfo"]
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return records