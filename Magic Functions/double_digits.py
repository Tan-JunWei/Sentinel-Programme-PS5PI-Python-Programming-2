def double_digits(num):
    '''
    Receives one integer – num, and returns it with each digit doubled.
    '''
    doubled_digits = map(lambda x: str(x) * 2 , str(num))
    return "".join(doubled_digits)

# >>> double_digits(542)
# 554422

print(double_digits(3))