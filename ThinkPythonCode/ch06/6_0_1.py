def is_between(x, y, z):
    return (x <= y <= z)


def inputRoutine():
    x = input("Please input x: ")
    y = input("Please input y: ")
    z = input("Please input z: ")
    # print(is_between(x,y,z):"1"?"2")
    if (is_between(x, y, z)):
        print("Yes")
    else:
        print("No")


inputRoutine()
