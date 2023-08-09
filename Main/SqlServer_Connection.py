import pyodbc

def get_SQL_Server_Connection():
    conn = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=your username;"
        "Database=System_Performance;"
        "Trusted_Connection=yes;"
    )
    return conn
















#
# def insert_data_into_sql_Server(data_to_insert):
#     conn = get_SQL_Server_Connection()
#
#     try:
#         insert_statement = f"INSERT INTO Performance (time	,cpu_usage	,memory_usage	,cpu_interrupts	,cpu_calls	,memory_used ,memory_free	,bytes_sent	,bytes_received	,disk_usage) VALUES (?,?,?,?,?,?,?,?,?,?)"
#
#         with conn.cursor() as cursor:
#             cursor.executemany(insert_statement, data_to_insert)
#
#         conn.commit()
#         print("Data insertion successful.")
#     except Exception as e:
#         print(f"Error occurred: {e}")
#     finally:
#         conn.close()
#
#
# while True:
#     current_datetime = datetime.datetime.now()
#     cpu_usage = psutil.cpu_percent()
#     memory_usage = psutil.virtual_memory()[2]
#     cpu_interrupts = psutil.cpu_stats()[1]
#     cpu_calls = psutil.cpu_stats()[3]
#     memory_used = psutil.virtual_memory()[3]
#     memory_free = psutil.virtual_memory()[4]
#     bytes_sent = psutil.net_io_counters()[0]
#     bytes_received = psutil.net_io_counters()[1]
#     disk_usage = psutil.disk_usage('/')[3]
#
#     data_to_insert = [
#         (current_datetime, cpu_usage, memory_usage, cpu_interrupts, cpu_calls, memory_used, memory_free, bytes_sent,
#          bytes_received, disk_usage)
#     ]
#
#     insert_data_into_sql_Server(data_to_insert)
#     print(current_datetime)
#     time.sleep(1)
