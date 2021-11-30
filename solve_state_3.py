import cube_3x3

cube = cube_3x3.cube()

def gen_possible_moves(moves:list):
    if not len(moves) == 0:
        omite_face = moves[-1]
    else:
        omite_face = " "
    faces = ["u", "d", "r", "l", "f", "b"]
    oposites = [["u", "d"], ["d", "u"], ["r", "l"], ["l", "r"], ["f", "b"], ["b", "f"]]
    possible_moves = []
    var = False
    for face in faces:
        if not omite_face == " ":
            if not omite_face[0] == face:
                if len(moves) >= 2:
                    for pair in oposites:
                        var = False
                        if pair[0] == face and pair[1] == omite_face[0] and face == moves[-2]:
                            var = True
                            break
                if var:
                    continue
                
                possible_moves.append(face+"2")

        else:
            possible_moves.append(face+"2")

            
    #print(omite_face, possible_moves)
    return possible_moves

def move(moves:list, scramble:str):
    cube = cube_3x3.cube()
    cube.scramble(scramble=scramble)
    
    for move in moves:
        cube.move(move)
    return (cube.solved_3(), cube.get_state())

def gen_moves(d:int, m_d:int, moves:list, possible_moves:list, scramble:str):
    if d == m_d:
        return (False, None, None)
    for i in range(len(possible_moves)):
        moves.append(possible_moves[i])
        solved = gen_moves(d+1, m_d, moves, gen_possible_moves(moves),scramble)
        if solved[0]:
            return solved
        if d == m_d-1:
            solved = move(moves, scramble)
            if solved[0]:
                return (solved[0], solved[1], moves)
        moves.pop(-1)
    return (False, None, None)

def solve(scramble:str):
    possible_moves = gen_possible_moves([])

    i = 0

    for i in range(20):
        solved = gen_moves(0, i, [], possible_moves, scramble)
        print(f"Step 3, depth: {i}")
        if solved[0]:
            break

    print(solved)
    cube = cube_3x3.cube()
    cube.scramble(solved[1])
    print(cube)
    return solved