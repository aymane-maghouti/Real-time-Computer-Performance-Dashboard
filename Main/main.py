from data_migration import from_mysql_to_sqlServer
from SqlServer_Connection import get_SQL_Server_Connection
from mysql_database_operations import insert_data_into_mysql,get_MySQL_connection
import time
import psutil
import datetime

while True:
    # system performance data
    current_datetime = datetime.datetime.now()
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory()[2]
    cpu_interrupts = psutil.cpu_stats()[1]
    cpu_calls = psutil.cpu_stats()[3]
    memory_used = psutil.virtual_memory()[3]
    memory_free = psutil.virtual_memory()[4]
    bytes_sent = psutil.net_io_counters()[0]
    bytes_received = psutil.net_io_counters()[1]
    disk_usage = psutil.disk_usage('/')[3]

    data_to_insert = [
        (current_datetime, cpu_usage, memory_usage,cpu_interrupts,cpu_calls,memory_used,memory_free,bytes_sent,bytes_received,disk_usage)
    ]

    insert_data_into_mysql(data_to_insert)
    time.sleep(1)

    Mysql_conn, table_name = get_MySQL_connection()
    sql_server_conn = get_SQL_Server_Connection()

    from_mysql_to_sqlServer(Mysql_conn,sql_server_conn,table_name)
