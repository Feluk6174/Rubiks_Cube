import game

solve = []

def check_moves(state, moves:list):
    #global solve
    print(state, id(state))
    g = None
    g = game.game(pos=state)
    #print(g)
    for move in moves:
        g.move(move)
    #print(g)
    if g.solved():
        return True
    return False


def gen_nums(d:int, m_d:int, moves:list, state = []):
    #global solve
    solve = []
    if d == m_d:
        return
    for i in range(3):
        moves.append(i)
        #print(moves)
        state = state
        print(state, id(state))
        if check_moves(state, moves):
            m = 0
            #print(moves)
            solve.append(moves)
            print(solve, moves, d)
            #t = 0/m
            """if len(moves) < len(solve) or solve == []:
                solve = moves
            break
            """
        #print(state, id(state))
        gen_nums(d+1, m_d, moves, state=state)
        moves.pop(len(moves)-1)
    return
gen_nums(0, 2, [], state=[3, 2, 1])

#check_moves([3, 2, 1], [0, 1 ,2, 2, 2])

#[0, 1, 2, 2, 2]
#[0, 0, 2, 1, 0, 1, 2, 1, 1, 1]
#[0, 0, 2, 1, 0, 2, 1, 1, 1, 0]

print(solve)