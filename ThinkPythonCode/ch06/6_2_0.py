def ack(m, n):
    if not ((isinstance(m, int)) and (isinstance(n, int))):
        print("'m' and 'n' shoule both be integer type.")
        return
    elif ((m < 0) or (n < 0)):
        print("'m' and 'n' shoule both be negitive.")
        return
    else:
        if (m == 0):
            return (n + 1)
        else:
            if (n == 0):
                return ack(m - 1, 1)
            else:
                return ack(m - 1, ack(m, n - 1))


m = input("Please input m: ")
n = input("Please input n: ")
print(ack(m, n))
