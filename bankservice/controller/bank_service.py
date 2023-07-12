from ..util.database_util import get_db_connection
from ..repo.bank_statement_repo import create_bank_statement
from ..repo.bank_statement_line_repo import create_bank_statement_lines
from ..model.bank_statement import validate_bank_statement
from ..model.bank_statement_line import validate_bank_statement_lines, validate_bank_statement_line
from ..util.date_util import db_date_format, basic_date_format, get_datetime, now


def process_and_save_new_bank_statement(data, statement_number, account_number):
    data_to_save = []
    start_date = None
    end_date = None
    running_balance = 0

    # Prepare data and validate
    for index, row in data.iterrows():
        date = row['Date']

        if start_date is None:
            start_date = date
        end_date = date

        description = row['Transactions']
        amount = float(row['Amount'])
        balance = float(row['Balance'])
        bank_line = (get_datetime(date, basic_date_format, db_date_format), description, amount, now(), now())

        # Validate bank statement lines
        errors = validate_bank_statement_line(bank_line[1], bank_line[2])
        if len(errors) != 0:
            raise Exception(", ".join(errors))

        # Check running balance
        if running_balance == 0:
            running_balance = balance - amount
        elif running_balance + amount < balance - 0.01 or running_balance + amount > balance + 0.01:
            raise Exception("The running balance and statement balance at line " + (
                        index + 1) + " do not match, please confirm that the bank statement is correct before uploading")

        data_to_save.append(bank_line)

    # Validate bank statement
    errors = validate_bank_statement(statement_number, account_number, start_date, end_date)
    if len(errors) != 0:
        raise Exception(", ".join(errors))

    # Save Data
    db_connection = get_db_connection()
    try:
        mycursor = db_connection.cursor()

        bank_statement = (statement_number, account_number, get_datetime(start_date, basic_date_format, db_date_format),
                          get_datetime(end_date, basic_date_format, db_date_format))
        create_bank_statement(bank_statement, db_connection, mycursor)
        statment_id = mycursor.lastrowid

        bank_statement_lines = [(statment_id,) + x for x in data_to_save]

        create_bank_statement_lines(bank_statement_lines, db_connection, mycursor)

        db_connection.commit()

    except Exception as e:
        db_connection.rollback()
        raise Exception(str(e))
    finally:
        db_connection.close()
