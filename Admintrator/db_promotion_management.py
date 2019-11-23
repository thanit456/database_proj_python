import mysql.connector
from mysql.connector import Error

# hyperparameter
databaseName = 'too_superstore'
tableName = 'promotion'
password = 'boss1234'

f = open('countPromotion.txt')
# global variable
countPromotionID = int(f.read())
f.close()

class Promotion() :
    def __init__(self, data) :
        self.promotionDataObj = PromotionDB(data)
        
    def write(self) :
        return self.promotionDataObj.writeDB(databaseName, tableName)
    
    def delete(self) :
        return self.promotionDataObj.deleteDB(databaseName, tableName)

    def getInfo(self) :
        return self.promotionDataObj.data

    def showTable(self):
        return self.promotionDataObj.showTable(databaseName, tableName)

    def edit(self):
        return self.promotionDataObj.editDB(databaseName, tableName)
    
    

class PromotionDB() :

    def __init__(self, data) :
        self.data = data
        self.columns = []
        self.records = []

    ##########################################################################

    def writeDB(self, databasename, table) :
        wdata=self.data
        global countPromotionID


        try:
            connection = mysql.connector.connect(host='localhost',database=databasename,user='root',password=password)

            objdata = (wdata[0], wdata[1], wdata[2], wdata[3], wdata[4])
                  
            sqlQuery = "insert into " + table +  " values ( '"+ str(countPromotionID) + "', '" + wdata[0] + \
                        "', '" + wdata[1] + "', " + wdata[2] + ", " + wdata[3] + ", '" + wdata[4]  + "')"

            cursor = connection.cursor()
            cursor.execute(sqlQuery)

            connection.commit()
            

        except:
            retmsg = ["1", "writing error"]
        else :
            retmsg = ["0", "writing done"]
            countPromotionID += 1
            f = open('countPromotion.txt', 'w')
            f.write(str(countPromotionID))
            f.close()
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg

          
    ##########################################################################
    def editDB(self, databasename, table) :

        try:
            connection = mysql.connector.connect(host='localhost',database=databasename,user='root',password=password)
               
            wdata = self.data
            objdata = (wdata[0], wdata[1], wdata[2], wdata[3], wdata[4], wdata[5])
                  
            print('object : ',objdata)

            sqlQuery = 'update promotion' + \
                    ' set StartDate = \'' + wdata[1] + "'" + \
                    ', EndDate = \'' + wdata[2]  + "'" + \
                    ', Percentage = ' + wdata[3]  + \
                    ', MemberPointCost = ' + wdata[4] + \
                    ', ProductID = \'' + wdata[5] + '\' ' + \
                    'where PromotionID = \'' + wdata[0] + "'"

            cursor = connection.cursor()
            cursor.execute(sqlQuery)

            connection.commit()
            

        except:
            retmsg = ["1", "editing error"]
        else :
            retmsg = ["0", "editing done"]
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg
    ##########################################################################
    def deleteDB(self, databasename, table) :
        wdata=self.data

        try:
            connection = mysql.connector.connect(host='localhost',database=databasename,user='root',password=password)
       
            objdata = (wdata[0],)
            
            sqlQuery = "DELETE FROM "+ table + " WHERE PromotionID = '" + wdata[0] + "'"
            print(sqlQuery)

            cursor = connection.cursor()
            cursor.execute(sqlQuery)
            connection.commit()

        except:
            retmsg = ["1", "delete error"]
        else :
            retmsg = ["0", "delete done"]
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg 
    ##########################################################################

    def showTable(self, databasename, table):
        try:
            connection = mysql.connector.connect(host='localhost', database=databasename, user='root', password=password)
            
            wdata = self.data
        

            if (wdata[0].strip() != '' and wdata[1].strip() != ''):
                sqlQuery = 'select * from ' + table + ' where PromotionID = "' + wdata[0].strip() + '" , ProductID = "' + wdata[1].strip()  + '"'
            elif (wdata[0].strip() != ''):
                sqlQuery = 'select * from ' + table + ' where PromotionID = "' + wdata[0].strip() + '"'
            elif (wdata[1].strip() != ''):
                sqlQuery = 'select * from' + table + ' where ProductID = "' + wdata[1].strip()  + '"'
            else:
                sqlQuery = "select * from " + table            
            print(sqlQuery)


            cursor = connection.cursor()
            cursor.execute(sqlQuery)
            self.records = cursor.fetchall()
            
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return self.records


             
        
        

