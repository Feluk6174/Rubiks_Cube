import game

solves = []

def solve(d, g, moves, pos, m_d=5):
    if not g.solved():
        if d == m_d:
            return False, []
        for i in range(3):
            temp_g = game.game(pos=pos)
            for move in moves:
                temp_g.move(move)
            moves.append(i)
            print(d, temp_g, moves)
            temp_g.move(i)
            if temp_g.solved():
                return True, moves
            s, s_moves = solve(d+1, temp_g, pos, moves)
            if s:
                #print(d, g, moves, "\n")
                return s, s_moves
            #print(moves)
            moves.pop(len(moves)-1)
            #print(moves)
            
        return False, []
    else:
        return True, moves

def temp_solve(d, moves, pos, m_d):
    global solves

    if d == m_d:
        return (False, [])
    for i in range(3):
        moves.append(i)
        g = game.game(pos=pos)
        for move in moves:
            g.move(move)
        if g.solved():
            return True, moves
        #print(moves)
        solved = temp_solve(d+1, moves, pos, m_d)
        print(solved)
        if solved[0]:
            return (True, moves)
        moves.pop(len(moves)-1)
    return (False, [])



def prove_moves(moves, g):
    for move in moves:
        print(g, move)
        g.move(move)
    print(g, g.solved())

def all_sates():
    global solves
    m_d = 4
    for x in range(10):
        for y in range(10):
            for z in range(10):
                g = game.game(pos=[x, y, z])
                init_pos = (g.pos[0], g.pos[1], g.pos[2])
                s = temp_solve(0, [], [x, y, z], m_d)
                print(s, init_pos)
                try:
                    temp = solves[-1]
                    solves.pop(len(solves)-1)
                    solves.append([[x, y, z], s, temp])
                except IndexError:
                    solves.append([[x, y, z], False])


g = game.game(pos=[0, 0, 1])

#s, moves = solve(0, g, [], [0,0,1])

print(temp_solve(0, [], [3, 2, 1], 10))

print(solves)

#s, moves = solve(0, g, [])
"""
all_sates()

t_res = 0
for res in solves:
    print(res)
    if res[0]:
        t_res += 1

print(t_res, len(solves))"""

#prove_moves(solves[1][3], game.game(pos=[solves[1][1][0],solves[1][1][1], solves[1][1][2]]))

#prove_moves(moves)