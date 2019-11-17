import mysql.connector
from mysql.connector import Error

# hyperparameter
databaseName = 'too_superstore'
tableName = 'promotion'
password = 'win448800'

class Product() :
    def __init__(self, data) :
        self.productDataObj = ProductDB(data)
    
    def search(self) :
        return self.productDataObj.searchDB(databaseName, tableName)

class ProductDB() :
    def __init__(self,data):
        self.data = data
    
    def searchDB(self, databaseName, table) :
        w.self = self.data

        try:
            connection = mysql.connector.connect(host='localhost',database=databaseName,user='root',password=password)
            
            # objdata = (BranchName,ProductName)
            objdata = (str(wdata[0]),str(wdata[1]))

            #Get branchID froim branchName to query in Product table
            sql_get_branchID = "select BranchID from branch where Name = %d"
            