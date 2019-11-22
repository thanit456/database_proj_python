import mysql.connector
from mysql.connector import Error

# hyperparameter
databaseName = 'too_superstore'
tableName = 'promotion'
password = '093128156'

# global variable
countPromotionID = 1

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

    def showTable(self):
        return self.promotionDataObj.showTable(databaseName, tableName)

    
    

class PromotionDB() :

    def __init__(self, data) :
        self.data = data
        self.columns = []
        self.records = []


    def writeDB(self, databasename, table) :
        wdata=self.data
        global countPromotionID


        try:
            connection = mysql.connector.connect(host='localhost',database=databasename,user='root',password=password)
       
            print('Can Connect')

            print('PromotionID : ' + str(countPromotionID))    
            countPromotionID += 1  

            objdata = (wdata[0], wdata[1], wdata[2], wdata[3], wdata[4])
                  
            sqlQuery = "insert into " + table +  " values ( '"+ str(countPromotionID) + "', '" + wdata[0] + \
                        "', '" + wdata[1] + "', " + wdata[2] + ", " + wdata[3] + ", '" + wdata[4]  + "')"
            print(sqlQuery)

            cursor = connection.cursor()
            cursor.execute(sqlQuery)

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

    # search by promotionID
    def searchDB(self, databasename, table) :
        wkey = str(self.data[0])

        try:
            connection = mysql.connector.connect(host='localhost',database=databasename,user='root',password='win448800')
            objdata = (wkey,)
            sqlQuery = "select * from "+table+" where PromotionID = %s"
            
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
            sqlQuery = "select * from "+table + " JOIN product ON ( promotion.ProductID == product.ProductID )" +" where ProductName = %s" #correct here
            
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

    # def showTable(self, databasename, table):
    #     try:
    #         connection = mysql.connector.connect(host='localhost', database=databasename, user='root', password=password)
    #         query_cols = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS  \
    #                 WHERE TABLE_NAME = '" + table + "' " + \
    #                 "ORDER BY ORDINAL_POSITION"
    #         cols_cursor = connection.cursor()
    #         cols_cursor.execute(query_cols)
    #         self.cols = cols_cursor.fetchall()

    #         sqlQuery = "select * from " + table
    #         cursor = connection.cursor()
    #         cursor.execute(sqlQuery)
    #         self.records = cursor.fetchall()
            
    #     except:
    #         retmsg  = ['1', 'Error']
    #     else:
    #         retmsg = ['1', 'Not Found']
    #         if self.cols[1] != '':
    #             retmsg = ['0', 'Found']        
    #     finally:
    #         if (connection.is_connected()):
    #             connection.close()
    #             cursor.close()
    #         return retmsg
    def showTable(self, databasename, table):
        try:
            connection = mysql.connector.connect(host='localhost', database=databasename, user='root', password=password)
            sqlQuery = "select * from " + table
            cursor = connection.cursor()
            cursor.execute(sqlQuery)
            self.records = cursor.fetchall()
            
        # except:
        #     retmsg  = ['1', 'Error']
        # else:
        #     retmsg = ['1', 'Not Found']
        #     if self.cols[1] != '':
        #         retmsg = ['0', 'Found']        
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return self.records


             
        
        

