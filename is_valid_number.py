def is_valid_number(input_str):
    if input_str.strip() and input_str.strip().isdigit() and int(input_str)>0:
        return True
    return False