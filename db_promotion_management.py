import mysql.connector
from mysql.connector import Error

# hyperparameter
databaseName = 'too_superstore'
tableName = 'promotion'
password = 'eieiza555'

# global variable
countPromotionID = 1
SIZE_PROMOTION_ID = 4

def getPromotionID():
    global countPromotionID
    if len(countPromotionID) > SIZE_PROMOTION_ID:
        return
    promotionID = ('0' * (SIZE_PROMOTION_ID - len(countPromotionID)) + str(countPromotionID))
    countPromotionID += 1
    return promotionID

class Promotion() :
    def __init__(self, data) :
        self.promotionDataObj = PromotionDB(data)
        
    def write(self) :
        return self.promotionDataObj.writeDB(databaseName, tableName)
        
    def search(self) :
        return self.promotionDataObj.searchDB(databaseName, tableName)
    
    def searchName(self) :
        return self.promotionDataObj.searchNameDB(databaseName, tableName)
    
    def delete(self) :
        return self.promotionDataObj.deleteDB(databaseName, tableName)

    def getInfo(self) :
        return self.promotionDataObj.data

    
    

class PromotionDB() :

    def __init__(self, data) :
        self.data = data


    def writeDB(self, databasename, table) :
        wdata=self.data

        try:
            connection = mysql.connector.connect(host='localhost',database=databasename,user='root',password=password)
       
            objdata = (wdata[0], wdata[1], wdata[2], wdata[3], wdata[4])
            
            # increment and get promotionID 
            promotionID = getPromotionID()

            sqlQuery = "insert into "+table+" (PromotionID, ProductID, StartDate, EndDate, Percentage, MemberPointCost) " \
                               "values ( "+ promotionID +", %s, %s, %s, %.2f, %d)"
            
            cursor = connection.cursor()
            cursor.execute(sqlQuery, objdata)
            
            connection.commit()
            

        except:
            retmsg = ["1", "writing error"]
        else :
            retmsg = ["0", "writing done"]
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg

          

    #writeDB("testdb", "test", ["0007","Somsiri"])
                
    ##########################################################################
    def deleteDB(self, databasename, table) :
        wdata=self.data

        try:
            connection = mysql.connector.connect(host='localhost',database=databasename,user='root',password=password)
       
            objdata = (wdata[0],)
            
            sqlQuery = "DELETE FROM "+ table + " WHERE PromotionID = %s"
            
            cursor = connection.cursor()
            cursor.execute(sqlQuery, objdata)
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

    def searchDB(self, databasename, table) :
        wkey = str(self.data[0])

        try:
            connection = mysql.connector.connect(host='localhost',database=databasename,user='root',password='win448800')
            objdata = (wkey,)
            sqlQuery = "select * from "+table+" where id = %s"
            
            cursor = connection.cursor()
            cursor.execute(sqlQuery, objdata)
            records = cursor.fetchone()
            self.data = records
                    
        except:
            retmsg = ["1", "Error"]
        else :
            retmsg = ["1", "Not Found"]
            if records[1] != "" :
                retmsg = ["0", "Found"]
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg


    ##########################################################################

    def searchNameDB(self, databasename, table) :
        wkey = str(self.data[1]) #correct here

        try:
            connection = mysql.connector.connect(host='localhost',database=databasename,user='root',password=password)
            objdata = (wkey,)
            sqlQuery = "select * from "+table+" where name = %s" #correct here
            
            cursor = connection.cursor()
            cursor.execute(sqlQuery, objdata)
            records = cursor.fetchone()
            self.data = records
                    
        except:
            retmsg = ["1", "Error"]
        else :
            retmsg = ["1", "Not Found"]
            if records[1] != "" :
                retmsg = ["0", "Found"]
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg





