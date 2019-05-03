import mysql.connector
from mysql.connector import Error

config = {
    'user': 'hubert',
    'password': 'hubert@MYSQL',
    'host': '127.0.0.1',
    'database': 'world',
    'raise_on_warnings': True
}

try:
    connection = mysql.connector.connect(**config)

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL database... MySQL Server version on ", db_Info)

        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Your connected to - ", record)

except Error as e:
    print("Error while connecting to MySQL: ", e)

finally:
    # closing database connection.
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
