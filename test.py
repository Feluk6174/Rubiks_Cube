import math, cube_3x3


def print_num(num:int, base:int, possible_moves:list):
    while num >= 1:
        print(possible_moves[num%base])
        num //= base

def convert(num:int, base:int, possible_moves:list, scramble:str, step:int):
    #moves = []
    cube = cube_3x3.cube()
    cube.scramble(scramble=scramble)
    while num >= 1:
        cube.move(possible_moves[num%base])
        num //= base
    if step == 0:
        return (cube.solved_0(), cube.get_state())
    elif step == 1:
        return (cube.solved_1(), cube.get_state())
    elif step == 2:
        return (cube.solved_2(), cube.get_state())
    elif step == 3:
        return (cube.solved_3(), cube.get_state())

possible_moves_0 = ['u', "u'", 'u2', 'd', "d'", 'd2', 'r', "r'", 'r2', 'l', "l'", 'l2', 'f', "f'", 'f2', 'b', "b'", 'b2']
possible_moves_1 = ['u', "u'", 'u2', 'd', "d'", 'd2', 'r2', 'l2', 'f', "f'", 'f2', 'b', "b'", 'b2']
possible_moves_2 = ['u', "u'", 'u2', 'd', "d'", 'd2', 'r2', 'l2', 'f2', 'b2']
possible_moves_3 = ['u2', 'd2', 'r2', 'l2', 'f2', 'b2']
scramble = "wwywwywwybbbggbooorrrrrrgggggggbbooorrrooobbbyyyyyywww"
cube = cube_3x3.cube()
cube.scramble()
scramble = cube.get_state()
print(scramble)

def gen(d:int, possible_moves:list, scramble:str, step:int):
    cube = cube_3x3.cube()
    cube.scramble(scramble=scramble)
    if step == 0 and cube.solved_0():
        return (0, cube.get_state())
    elif step == 1 and cube.solved_1():
        return (0, cube.get_state())
    elif step == 2 and cube.solved_2():
        return (0, cube.get_state())
    elif step == 3 and cube.solved_3():
        return (0, cube.get_state())
        
    for i in range(int(math.pow(len(possible_moves), d))):
        solved = convert(i, len(possible_moves), possible_moves, scramble, step)
        print(i)
        if solved[0]:
            return (i, solved[1])


solved_0 = gen(20, possible_moves_0, scramble, 0)
print(solved_0, print_num(solved_0[0], len(possible_moves_0), possible_moves_0))
solved_1 = gen(20, possible_moves_1, solved_0[1], 1)
print(solved_1, print_num(solved_1[0], len(possible_moves_1), possible_moves_1))
solved_2 = gen(20, possible_moves_2, solved_1[1], 2)
print(solved_2, print_num(solved_2[0], len(possible_moves_2), possible_moves_2))
solved_3 = gen(20, possible_moves_3, solved_2[1], 3)
print(solved_3, print_num(solved_3[0], len(possible_moves_3), possible_moves_3))
print("solves -------------------------------------------------------------------------------")
print_num(solved_0[0], len(possible_moves_0), possible_moves_0)
print_num(solved_1[0], len(possible_moves_1), possible_moves_1)
print_num(solved_2[0], len(possible_moves_2), possible_moves_2)
print_num(solved_3[0], len(possible_moves_3), possible_moves_3)