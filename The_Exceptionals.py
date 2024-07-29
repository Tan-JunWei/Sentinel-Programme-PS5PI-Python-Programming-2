# Your task
# Implement the following functions, each causing their specified exception to be raised when called, without using the raise keyword.

# For example: raise_zero_division_error will raise ZeroDivisionError when called, without using the line raise ZeroDivisionError.
# raise_zero_division_error()
# raise_attribute_error()
# raise_import_error()
# raise_index_error()
# raise_key_error()
# raise_name_error()
# raise_type_error()
# raise_value_error()
# raise_file_not_found_error()
# Use the the_exceptionals.py as a starting point.

def raise_zero_division_error():
    return 1/0

def raise_attribute_error():
    x = 10
    return x.append(6)

def raise_import_error():
    import nonexistentmodule

def raise_index_error():
    x = [10]
    return x[2]

def raise_key_error(): 
    dict = {"a":1}
    return dict["b"]

def raise_name_error():
    _ = nonexistentvariable

def raise_type_error():
    x = "a"
    return x+1

def raise_value_error():
    int("dejfjfbjfjrejfejs")

def raise_file_not_found_error():
    open("fskfnrswf.txt")

try:
    raise_zero_division_error()
except ZeroDivisionError:
    print("ZeroDivisionError caught")

try:
    raise_attribute_error()
except AttributeError:
    print("AttributeError caught")

try:
    raise_import_error()
except ImportError:
    print("ImportError caught")

try:
    raise_index_error()
except IndexError:
    print("IndexError caught")

try:
    raise_key_error()
except KeyError:
    print("KeyError caught")

try:
    raise_name_error()
except NameError:
    print("NameError caught")

try:
    raise_type_error()
except TypeError:
    print("TypeError caught")

try:
    raise_value_error()
except ValueError:
    print("ValueError caught")

try:
    raise_file_not_found_error()
except FileNotFoundError:
    print("FileNotFoundError caught")