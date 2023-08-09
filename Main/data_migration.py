def from_mysql_to_sqlServer(Mysql_conn,sql_server_conn,table_name):
    cursor_mysql = Mysql_conn.cursor()
    cursor_sql_server = sql_server_conn.cursor()

    extract = "SELECT * FROM performance ORDER BY time DESC LIMIT 1"
    cursor_mysql.execute(extract)

    for row in cursor_mysql.fetchall():

        insert_query = f"INSERT INTO {table_name} VALUES (?, ?, ?,?, ?, ?,?, ?, ?,?)"

        values = (row[0], row[1], row[2],row[3],row[4],row[5], row[6], row[7],row[8],row[9])

        cursor_sql_server.execute(insert_query, values)
        sql_server_conn.commit()
        print("Data insertion successful into SQL Server Database.")



