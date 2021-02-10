import mysql.connector

database_movie = (
    mysql
    .connector
    .connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'online_movie_rating'
    )
)

def drop_table(database, table_name):
    drop_query = (
        f"""
        DROP TABLE IF EXISTS {table_name}
        """
    )
    cursor = database.cursor()
    cursor.execute(drop_query)
    database.commit()
    print('table has been dropped!')

def create_table(database):
    movies_table_query = (
    """
        CREATE TABLE movies(
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(100),
        release_year YEAR(4),
        collection_in_mil_dol INT
        )
        """
    )

    reviewer_table_query = (
        """
        CREATE TABLE reviewers(
        id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(100),
        last_name VARCHAR(100)
        )
    """
    )

    cursor = database.cursor()
    cursor.execute(movies_table_query)
    cursor.execute(reviewer_table_query)
    database.commit()
    print('create tables have done!')

def insert_data(database, movie_list):
    insert_query = (
        """
        INSERT INTO movies (title, release_year, collection_in_mil_dol) 
        VALUES (%s, %s, %s)
        """
    )
    cursor = database.cursor()
    cursor.executemany(insert_query, movie_list)
    database.commit()
    print('data inserted!')


def show_data(database, table_name):
    search_query = (
        f"""
        SELECT * FROM {table_name}
        """
    )
    cursor = database.cursor()
    cursor.execute(search_query)
    output = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        print(output)
    
def update_data(database, id, title, release_year, collection_in_mil_dol):
    update_query = ( 
        
        "UPDATE movies set title='"+title+"', release_year='"+release_year+"', collection_in_mil_dol='"+str(collection_in_mil_dol)+"' where id="+id+" "
    )
    cursor = database.cursor()
    cursor.execute(update_query)
    database.commit()
    print('data updated!')


def delete_data(database, table_name, id_table):

    delete_query = (
        f"""
        DELETE FROM {table_name} WHERE id= {id_table}
        """
    )

    cursor = database.cursor()
    cursor.execute(delete_query)
    database.commit()
    print('data deleted!')

def search_data(database, table_name, id_table):
    search_query = (
        f"""
        SELECT * FROM {table_name} WHERE id LIKE {id_table}
        """
    )
    cursor = database.cursor()
    cursor.execute(search_query)
    output = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        print(output)

def show_menu(database):
  print("=== APLIKASI DATABASE PYTHON ===")
  print("1. Insert Data")
  print("2. Tampilkan Data")
  print("3. Update Data")
  print("4. Hapus Data")
  print("5. Cari Data")
  print("0. Keluar")
  print("------------------")
  menu = input("Pilih menu> ")

  if menu == "1":
    insert_data(database, movie_list)
  elif menu == "2":
    show_data(database, table_name)  
  elif menu == "3":
    update_data(database, id, title, release_year, collection_in_mil_dol)
  elif menu == "4":
    delete_data(database, table_name, id_table)
  elif menu == "5":
    search_data(database, table_name, id_table)
  elif menu == "0":
    exit()
  else:
    print("Menu salah!")


if __name__ == "__main__":
  while(True):
    show_menu(database_movie)



