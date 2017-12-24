def is_power(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        return False
    if ((a <= 0) or (b <= 0)):
        return False
    
    if ((b==1) and (a != 1)):
        return False
    if (a == b):
        return True
    if ((a % b == 0) and (is_power(a / b, b))):
        return True

    return False


# a = raw_input('Please input a: ')
# b = raw_input('Please input b: ')
a = input('Please input a: ')
b = input('Please input b: ')
print(is_power(a, b))
