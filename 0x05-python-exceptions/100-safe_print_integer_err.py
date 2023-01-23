#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return False
    return True