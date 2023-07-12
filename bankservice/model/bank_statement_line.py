def validate_bank_statement_lines(lines):
    errors = []

    return errors


def validate_bank_statement_line(description, amount):
    errors = []

    if not amount.isnumeric():
        errors.append("Incorrect value for amount")

    return errors
