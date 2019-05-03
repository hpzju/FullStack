import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="hubert",
    passwd="hubert@MYSQL"
)
mycursor = mydb.cursor()


def main():
    mycursor.execute("SHOW DATABASES;")
    for db in mycursor:
        print(db)


if __name__ == "__main__":
    main()
