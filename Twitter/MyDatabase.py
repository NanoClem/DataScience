import mysql.connector as mysql


class MyDatabase :
    """
    """

    def __init__(self, _host = "localhost", _user="root", _password="root", _port="3306") :
        """
        CONSTRUCTEUR de la classe MyDatabase
        ATTRIBUTE host : nom d'hote de la bdd
        ATTRIBUTE user : nom d'utilisateur
        ATTRIBUTE password : mot de passe
        ATTRIBUTE mydb : objet PDO
        """
        self.host     = _host
        self.user     = _user
        self.password = _password
        self.port     = _port
        self.mydb     = None



    def connectToMySQL(self) :
        """
        Connexion au domaine mysql
        """
        self.mydb = mysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            passwd = self.password
        )



    def connectToDB(self, DBname) :
        """
        Connexion a la base de donnee
        passee en parametre
        PARAM DBname : nom de la bdd
        """
        self.mydb = mysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            passwd = self.password,
            database = DBname
        )



    def createDatabase(self, DBname) :
        """
        Creation d'une nouvelle base de donnees
        Si la bdd existe deja, affiche un message d'erreur
        PARAM DBname : nom de la bdd a creer
        """
        mycursor = self.mydb.cursor()
        mycursor.execute("SHOW DATABASES ")
        if DBname in mycursor :
            print("ERROR : Database already existing")
        else :
            mycursor.execute("CREATE DATABASE " + DBname)
            print("Successfuly created database %s" %DBname)



    def createTable(self, tableName, cols = {}) :
        """
        Creation d'une nouvelle table dans
        la bdd courrante
        PARAM tableName : nom de la table a creer
        PARAM cols : informations sur les colonnes de la table (nom/type)
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
        Insertion de donnees dans la table
        passee en parametre
        PARAM tableName : nom de la table
        PARAM toInsert : description des donnees a inserer
        """
        mycursor = self.mydb.cursor()
        columns = val = ""
        for key,value in toInsert.items() :
            columns += key
            val     += str(value)
            if key != list(toInsert.keys())[-1] :
                columns += ", "
                val     += ", "

        sql = "INSERT INTO %s (%s) VALUES(%s)" %(tableName, columns, val)
        print(sql)
        mycursor.execute(sql)
        self.mydb.commit()
        print(mycursor.rowcount, "record inserted")
