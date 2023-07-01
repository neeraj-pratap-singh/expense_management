import re

date_pattern = r'^\d{4}-\d{2}-\d{2}$'

def is_valid_date(date_string):
    if re.match(date_pattern, date_string):
        return True
    return False
