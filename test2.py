import time

def timer():
    def gen_moves(d:int, m_d:int, moves:list, possible_moves:list):
        if d == m_d:
            return
        for i in range(len(possible_moves)):
            moves.append(possible_moves[i])
            solved = gen_moves(d+1, m_d, moves, possible_moves)
            if d == m_d-1:
                pass
                #print(moves)
            moves.pop(-1)

    faces = ["u", "d", "r", "l", "f", "b"]
    possible_moves = []
    for face in faces:
        possible_moves.append(face)
        possible_moves.append(face+"'")
        possible_moves.append(face+"2")

    print(t_1:=time.time())

    gen_moves(0, 3, [], possible_moves)

    print(t_2:=time.time())
    return t_2-t_1