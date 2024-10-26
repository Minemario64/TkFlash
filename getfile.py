from sqlite3 import *

def is_db_empty(db_path):

    conn = connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    if not tables:
        conn.close()
        return True

def tkflash_query_db(db : str, dbTable : str, dbColumnList : list[str], dbCallList : list[int], class_id : int, allColumns : bool = True):

    connection = connect(db)
    cursor = connection.cursor()

    if allColumns:
        cursor.execute(f"SELECT * FROM {dbTable} WHERE class_id = {class_id};")
    else:
        i = 0
        for column in dbCallList:
            i += 1
            if i == 1:
                qcolumn = f"{dbColumnList[column]}, "
            else:
                qcolumn += f"{dbColumnList[column]}, "
        qcolumn = qcolumn[:-2]

        cursor.execute(f"SELECT {qcolumn} FROM {dbTable} WHERE class_id = {class_id};")
        print(cursor.fetchall())

        connection.commit()
        connection.close()