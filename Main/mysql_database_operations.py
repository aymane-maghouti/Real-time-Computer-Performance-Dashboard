import mysql.connector


def get_MySQL_connection():
    host = 'localhost'
    database = 'system_Performance'
    user = 'root'
    password = ''
    table_name = 'performance'

    connection = mysql.connector.connect(host=host, database=database, user=user, password=password)
    return connection,table_name


def insert_data_into_mysql(data_to_insert):
    connection,table_name = get_MySQL_connection()

    try:
        insert_statement = f"INSERT INTO {table_name} (time	,cpu_usage	,memory_usage	,cpu_interrupts	,cpu_calls	,memory_used ,memory_free	,bytes_sent	,bytes_received	,disk_usage) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s)"

        with connection.cursor() as cursor:
            cursor.executemany(insert_statement, data_to_insert)

        connection.commit()
        print("Data insertion successful into MySQL Database.")
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        connection.commit()













