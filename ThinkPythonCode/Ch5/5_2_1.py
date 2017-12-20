def check_fermat(a, b, c, n):
    noInfo = "No, that doesn't work."
    yesInfo = "Holy smokes, Fermat was wrong!"
    inputErrInfo = "Please make sure 'no positive integers a, b, and c', and 'n > 2'"
    a = int(a)
    b = int(b)
    c = int(c)
    n = int(n)
    if (n > 2) and (a > 0) and (b > 0) and (c > 0):
        valueOnLeft = a**n + b**n
        valueOnRight = c**n
        if (valueOnLeft == valueOnRight):
            print(yesInfo)
        else:
            print(noInfo)
    else:
        print(inputErrInfo)


a = input("Please input a: ")
b = input("Please input b: ")
c = input("Please input c: ")
n = input("Please input n: ")
print("**********************")
check_fermat(a, b, c, n)
print("")