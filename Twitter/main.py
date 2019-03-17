from MyDatabase import MyDatabase



def main() :
    #INFORMATIONS SUR LA BDD
    TwiDatabase = "twitterdatabase"                 # Attention : pas de majuscule dans le nom
    cols = {                                        # description des colonnes
        "idUser"   : "VARCHAR(200) NOT NULL PRIMARY KEY",
        "pseudo"   : "VARCHAR(50)",
        "location" : "VARCHAR(30)"
    }
    toInsert = {                                    # donnees a inserer
        "idUser"   : 55545256,
        "pseudo"   : "Kikoo",
        "location" : "France"
    }

    db = MyDatabase()

    #CREATION ET CONNECTION A LA BDD
    db.connectToMySQL()
    # db.createDatabase(TwiDatabase)
    db.connectToDB(TwiDatabase)

    #OPERATION SUR LA BDD
    # db.createTable("User", cols)
    db.insert("user", toInsert)



if __name__ == '__main__':
    main()
