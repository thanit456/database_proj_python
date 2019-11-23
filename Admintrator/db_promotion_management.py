import mysql.connector
from mysql.connector import Error

# hyperparameter
databaseName = 'too_superstore'
tableName = 'promotion'
password = '093128156'

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

            objdata = (wdata[0], wdata[1], wdata[2], wdata[3], wdata[4], wdata[5])

            # insert into promotion table  
            sqlQuery = "insert into " + table +  " values ( '"+ str(countPromotionID) + "', '" + wdata[0] + \
                        "', '" + wdata[1] + "', " + wdata[2] + ", " + wdata[3] + ", '" + wdata[4]  + "') ;"

            print('Query : ', sqlQuery)
            cursor = connection.cursor()
            cursor.execute(sqlQuery)
            connection.commit()

            # ! insert into salesat table
            sup_sqlQuery = "insert into salesat  values ( '" + str(countPromotionID) + "',  '" + wdata[5] + "' );"
            print('Sub query : ', sup_sqlQuery)
            cursor = connection.cursor()
            cursor.execute(sup_sqlQuery)
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
            objdata = (wdata[0], wdata[1], wdata[2], wdata[3], wdata[4], wdata[5], wdata[6])

             # ! delete old salesat
            delete_old_sqlQuery = 'delete from sales where PromotionID = "' + wdata[0] + '", BranchID = "' + wdata[6]  + '"'
            print('Delete old salesat : ', delete_old_sqlQuery)
            cursor = connection.cursor()
            cursor.execute(delete_old_sqlQuery)
            connection.commit()

            # ! inserte new salesat 
            insert_new_sqlQuery = 'insert into salesat values ("' + wdata[0] + '", "' + wdata[6] + '")'
            print('Insert new salesat : ', insert_new_sqlQuery)
            cursor = connection.cursor()
            cursor.execute(insert_new_sqlQuery)
            connection.commit()

            # ? update promotion
            sqlQuery = 'update promotion' + \
                    ' set StartDate = \'' + wdata[1] + "'" + \
                    ', EndDate = \'' + wdata[2]  + "'" + \
                    ', Percentage = ' + wdata[3]  + \
                    ', MemberPointCost = ' + wdata[4] + \
                    ', ProductID = \'' + wdata[5] + '\' ' + \
                    'where PromotionID = \'' + wdata[0] + "'"
            print('Edit : ', sqlQuery)
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
            

            sup_sqlQuery = "DELETE FROM salesat WHERE PromotionID = '" + wdata[0] + "'"
            print(sup_sqlQuery)
            cursor = connection.cursor()
            cursor.execute(sup_sqlQuery)
            connection.commit()

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
        

            sqlQuery = 'select * from ' + table + " NATURAL JOIN salesat"
            if (wdata[0].strip() != '' and wdata[1].strip() != '' and wdata[2].strip() != ''):
                sqlQuery += ' where PromotionID = "' + wdata[0].strip() + '" and ProductID = "' + wdata[1].strip()  + '"and BranchID = "' + wdata[2].strip() + '"'
            elif (wdata[0].strip() != '' and wdata[1].strip() != ''):
                sqlQuery += ' where PromotionID = "' + wdata[0].strip() + '" and ProductID = "' + wdata[1].strip() + '"'
            elif (wdata[0].strip() != '' and wdata[2].strip() != ''):
                sqlQuery += ' where PromotionID = "' + wdata[0].strip() + '" and BranchID = "' + wdata[1].strip() + '"'
            elif (wdata[1].strip() != '' and wdata[2].strip() != ''):
                sqlQuery += ' where ProductID = "' + wdata[1].strip()  + '" and  BranchID = "' + wdata[2].strip() + '"'
            elif (wdata[0].strip() != ''):
                sqlQuery += ' where PromotionID = "' + wdata[0].strip() + '"'
            elif (wdata[1].strip() != ''):
                sqlQuery += ' where ProductID = "' + wdata[1].strip() + '"'
            elif (wdata[2].strip() != ''):
                sqlQuery += ' where BranchID = "' + wdata[2].strip() + '"'

            print(sqlQuery)


            cursor = connection.cursor()
            cursor.execute(sqlQuery)
            self.records = cursor.fetchall()
            
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return self.records


             
        
        

