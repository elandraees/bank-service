import mysql.connector


def get_db_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="zxcvbnm",
        database="mydb"
    )
    return mydb

def get_query_results(sql, val, mycursor, db_connector):
    commit = False
    if db_connector is None:
        db_connector = get_db_connection()
        commit = True

    try:
        if mycursor is None:
            mycursor = db_connector.cursor()
        mycursor.execute(sql, val)

        return mycursor.fetchall()

    except Exception as e:
        if commit:
            db_connector.rollback()
        raise Exception('Unable to execute query: ' + str(e))
    finally:
        if commit:
            db_connector.commit()

def insert_into_db(sql, val, mycursor, db_connector):
    commit = False
    if db_connector is None:
        db_connector = get_db_connection()
        commit = True

    try:
        if mycursor is None:
            mycursor = db_connector.cursor()
        mycursor.execute(sql, val)
    except Exception as e:
        if commit:
            db_connector.rollback()
        raise Exception('Unable to execute query: ' + str(e))
    finally:
        if commit:
            db_connector.commit()

def insert_many_into_db(sql, val, mycursor, db_connector):
    commit = False
    if db_connector is None:
        db_connector = get_db_connection()
        commit = True

    try:
        if mycursor is None:
            mycursor = db_connector.cursor()
        mycursor.executemany(sql, val)
    except Exception as e:
        if commit:
            db_connector.rollback()
        raise Exception('Unable to execute query: ' + str(e))
    finally:
        if commit:
            db_connector.commit()
