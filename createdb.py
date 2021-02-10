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

def create_database(connection):
    cursor = connection.cursor()
    cursor.execute('CREATE DATABASE online_movie_rating')
    print('database created!')

def delete_database(connection):
    cursor = connection.cursor()
    cursor.execute('DROP DATABASE toko_mainan')
    print('database deleted!')


if __name__ == '__main__':
    create_database(database_connection)
    # create_database(database_connection)