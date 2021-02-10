import mysql.connector


database_connection = (
    mysql
    .connector
    .connect(
        host='localhost',
        user=input('user = '),
        password=input('password = ')
    )
)

if database_connection.is_connected():
    print('connected!')
