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

                possible_moves.append(face)
                possible_moves.append(face+"'")
                possible_moves.append(face+"2")
        else:
            possible_moves.append(face)
            possible_moves.append(face+"'")
            possible_moves.append(face+"2")

            
    #print(omite_face, possible_moves)
    return possible_moves

def move(moves:list):
    scramble = "wyywwywwyggbggbggbrrorrorrobbgbbgbbgoorooroorywwyywyyw"
    cube = cube_3x3.cube()
    cube.move("u")
    cube.move("d2")
    cube.move("r2")
    cube.move("l")
    cube.move("f")
    
    for move in moves:
        cube.move(move)
    if cube.solved_0():
        print(cube)
    return cube.solved_0()

def gen_moves(d:int, m_d:int, moves:list, possible_moves:list):
    if d == m_d:
        return
    for i in range(len(possible_moves)):
        moves.append(possible_moves[i])
        print(moves)
        if gen_moves(d+1, m_d, moves, gen_possible_moves(moves)):
            return True
        if move(moves):
            return True
        moves.pop(-1)

possible_moves = gen_possible_moves([])

print(possible_moves)

i = 0

while True:
    if gen_moves(0, i, [], possible_moves):
        break
    i += 1

#import solve_state_3