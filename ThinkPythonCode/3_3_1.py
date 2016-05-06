#print('+ ', '- '*4, '+ ', '- '*4, '+')
#print('|', ' '*9, '|', ' '*9, '|')
#print('+', end=' ')
#print('-')


def print_edge():
    print('+ ', '- '*4, '+ ', '- '*4, '+')
    
def print_midLine():
    print('|', ' '*9, '|', ' '*9, '|')
    
def print_oneCycle():
    print_edge()
    print()
    print_midLine()
    print()
    print_midLine()
    print()
    print_midLine()
    print()
    print_midLine()
 
print_oneCycle()
print_oneCycle()
print_edge()
