import math

def print_num(num:int, base:int, possible_moves:list):
    i = 0
    moves = []
    if num == 0:
        return
    for i in range(int(math.log(num, base))+1):
        moves.append(possible_moves[num%base])
        print(i, num)
        i+=1
        num //= base
    print(moves)

for i in range(int(math.pow(18, 3))):
    pass
    print_num(i, 18, ['u', "u'", 'u2', 'd', "d'", 'd2', 'r', "r'", 'r2', 'l', "l'", 'l2', 'f', "f'", 'f2', 'b', "b'", 'b2'])

#print(print_num(324, 18, ['u', "u'", 'u2', 'd', "d'", 'd2', 'r', "r'", 'r2', 'l', "l'", 'l2', 'f', "f'", 'f2', 'b', "b'", 'b2']))
#print(print_num(323, 18, ['u', "u'", 'u2', 'd', "d'", 'd2', 'r', "r'", 'r2', 'l', "l'", 'l2', 'f', "f'", 'f2', 'b', "b'", 'b2']))