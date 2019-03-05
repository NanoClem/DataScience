import mysql.connector as mysql


class MyDatabase :
    """
    """

    def __init__(self, _host = "localhost", _user="root", _password="root") :
        """
        """
        self.host     = _host
        self.user     = _user
        self.password = _password
        self.mydb     = None



    def connectToMySQL(self) :
        """
        """
        self.mydb = mysql.connect(
            host = self.host,
            user = self.user,
            passwd = self.password
        )



    def connectToDB(self, DBname) :
        """
        """
        self.mydb = mysql.connect(
            host = self.host,
            user = self.user,
            passwd = self.password,
            database = DBname
        )



    def createDatabase(self, DBname) :
        """
        """
        mycursor = self.mydb.cursor()
        mycursor.execute("SHOW DATABASES ")
        if DBname in mycursor :
            print("Database already existing")
        else :
            mycursor.execute("CREATE DATABASE " + DBname)
            print("Successfuly created database %s" %DBname)



    def createTable(self, tableName, cols = {}) :
        """
        """
        mycursor = self.mydb.cursor()
        sql  = ""
        for key,value in cols.items() :
            sql += key + " " + str(value)
            if key != list(cols.keys())[-1] :     #derniere colonne du dicionnaire
                sql += ", "

        print("CREATE TABLE %s (%s)" %(tableName,sql))
        mycursor.execute("CREATE TABLE %s (%s)" %(tableName,sql))



    def insert(self, tableName, toInsert = {}) :
        """
        """
        mycursor = self.mydb.cursor()
        columns = val = ""
        for key,value in toInsert.items() :
            columns += key
            val     += str(value)
            if key != list(cols.keys())[-1] :
                columns += ", "
                val     += ", "

        sql = "INSERT INTO %s (%s) VALUES(%s)" %(tableName, columns, val)
        print(sql)
        mycursor.execute(sql)
        self.mydb.commit()
        print(mycursor.rowcount, "record inserted")




if __name__ == '__main__':
    #COLONNES DE LA TABLE USER
    TwiDatabase = "TwitterDatabase"
    cols = {
        "idUser"   : "VARCHAR(200) PRIMARY KEY",
        "pseudo"   : "VARCHAR(50)",
        "location" : "VARCHAR(30)"
    }
    toInsert = {
        "idUser"   : 55545256,
        "pseudo"   : "Kikoo",
        "location" : "France"
    }

    db = MyDatabase()
    db.connectToMySQL()
    db.createDatabase(TwiDatabase)
    db.connectToDB(TwiDatabase)
    db.createTable("User", cols)
    db.insert("User", toInsert)
