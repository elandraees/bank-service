def is_none_empty_or_zero(value):
    if value is None:
        return True
    if value.isnumeric() and value == 0:
        return True
    if isinstance(value, str) and len(value) == 0:
        return True
    return False
