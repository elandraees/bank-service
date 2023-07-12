from ..util.database_util import insert_into_db, get_query_results


def create_bank_statement(data_tuple, db_connector, mycursor):
    sql = "INSERT INTO bank_statement (statement_number, account_number, start_date, end_date) VALUES (%s, %s, %s, %s)"
    val = data_tuple
    insert_into_db(sql, val, mycursor, db_connector)


def get_bank_statement_for_account_number_and_date(account_number, start_date, end_date):
    sql = "select * from bank_statement where account_number = %s and " \
          "(start_date <= %s and end_date >= %s )" \
          "OR (start_date <= %s and end_date >= %s)" \
          "OR (start_date <= %s and end_date >= %s )"
    val = (account_number, end_date, start_date, start_date, end_date, start_date, end_date)
    return get_query_results(sql, val, None, None)
