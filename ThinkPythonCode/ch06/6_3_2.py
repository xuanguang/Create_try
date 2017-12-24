def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]

def is_palindrome(str):
    if (len(str) <=1):
    # if (str == ''):
        return True
    else:
        if (first(str) != last(str)):
            return False
        else:
            return is_palindrome(middle(str))
        
str1 = raw_input("Please input a string: ")
print(str1)
print(is_palindrome(str1))