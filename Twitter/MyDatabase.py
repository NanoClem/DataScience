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
        columns  = ""
        for key,value in cols.items() :
            columns += key + " " + str(value)
            if key != list(cols.keys())[-1] :     #derniere colonne du dicionnaire
                columns += ", "

        print("CREATE TABLE %s (%s)" %(tableName,columns))
        mycursor.execute("CREATE TABLE %s (%s)" %(tableName,columns))



if __name__ == '__main__':
    #COLONNES DE LA TABLE USER
    cols = {
        "idUser"   : "VARCHAR(255)",
        "pseudo"   : "VARCHAR(50)",
        "location" : "VARCHAR(30)"
    }

    db = MyDatabase()
    db.connectToMySQL()
    db.connectToDB("TwitterDatabase")
    db.createTable("User", cols)
