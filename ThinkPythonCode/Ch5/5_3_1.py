def is_triangle(a, b, c):
    if (a <= 0) or (b <= 0) or (c <= 0):
        print("No")
        return
    # min_stick = min(a,b,c)
    sticks = sorted([a, b, c])
    if (sticks[0] + sticks[1] > sticks[2]):
        print('Yes')
    else:
        print('No')


def handle_input():
    a = input('Please input the stick - a: ')
    a = int(a)
    b = input('Please input the stick - b: ')
    b = int(b)
    c = input('Please input the stick - c: ')
    c = int(c)
    is_triangle(a, b, c)


handle_input()
