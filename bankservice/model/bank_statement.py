from ..util.validation_util import is_none_empty_or_zero
from ..repo.bank_statement_repo import get_bank_statement_for_account_number_and_date


def validate_bank_statement(statement_number, account_number, start_date, end_date):
    errors = []

    if is_none_empty_or_zero(statement_number):
        errors.append("No bank statement number found.")

    if is_none_empty_or_zero(account_number):
        errors.append("No bank account number found.")

    # Check for duplicate
    if len(errors) == 0:
        duplicates = get_bank_statement_for_account_number_and_date(account_number, start_date, end_date)
        if len(duplicates) > 0:
            errors.append("Duplicate bank statements found.")

    return errors
