from ..util.database_util import insert_many_into_db


def create_bank_statement_lines(data_tuple, db_connector, mycursor):
    sql = "INSERT INTO bank_statement_line (bank_statement_id, transaction_date, description, " \
          "amount, create_date, last_update) VALUES (%s, %s, %s, %s, %s, %s)"
    val = data_tuple
    insert_many_into_db(sql, val, mycursor, db_connector)
