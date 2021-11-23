import cube_3x3

def gen_possible_moves_0(moves:list):
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

    return possible_moves


def gen_possible_moves_1(moves:list):
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
                if not face == "r" and not face == "l":
                    possible_moves.append(face)
                    possible_moves.append(face+"'")
                    possible_moves.append(face+"2")
                else:
                    possible_moves.append(face+"2")

        else:
            if not face == "r" or not face == "l":
                possible_moves.append(face)
                possible_moves.append(face+"'")
                possible_moves.append(face+"2")
            else:
                possible_moves.append(face+"2")

            
    #print(omite_face, possible_moves)
    return possible_moves


def gen_possible_moves_2(moves:list):
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
                if face == "u" or face == "d":
                    possible_moves.append(face)
                    possible_moves.append(face+"'")
                    possible_moves.append(face+"2")
                else:
                    possible_moves.append(face+"2")

        else:
            if face == "u" or face == "d":
                possible_moves.append(face)
                possible_moves.append(face+"'")
                possible_moves.append(face+"2")
            else:
                possible_moves.append(face+"2")

            
    #print(omite_face, possible_moves)
    return possible_moves


def gen_possible_moves_3(moves:list):
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

    return possible_moves





def move_0(moves:list):
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


def move_1(moves:list):
    scramble = "wyywwywwyggbggbggbrrorrorrobbgbbgbbgoorooroorywwyywyyw"
    cube = cube_3x3.cube()
    cube.move("u")
    cube.move("f")
    cube.move("r2")
    
    for move in moves:
        cube.move(move)
    if cube.solved_1():
        print(cube)
    return cube.solved_1()