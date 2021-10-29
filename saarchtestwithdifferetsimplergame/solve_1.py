import game

pos = [0, 1, 1]

def check_moves(pos, moves:list):
	#global pos
	g = game.game(pos = pos)
	for move in moves:
		g.move(move)
		
	return g.solved()
				
def solve(d, moves, m_d):
	if d == m_d:
		return False
	pos = [0, 0, 0]
	with open("test.txt", "r") as f:
		text = f.read()
		pos[0] = int(text[0])
		pos[1] = int(text[1])
		pos[2] = int(text[2])
	if check_moves(pos,moves):
		return True
	for i in range(3):
		moves.append(i)
		pos = [0, 0, 0]
		with open("test.txt", "r") as f:
			text = f.read()
			pos[0] = int(text[0])
			pos[1] = int(text[1])
			pos[2] = int(text[2])
		if check_moves(pos,moves):
			return True
		s = solve(d+1, moves, m_d)
		if s:
			return s
		moves.pop(-1)
	return False
		
def gen_pos(m_d):
	for i in range(10):
		for j in range(10):
			for k in range(10):
				with open("test.txt", "w") as f:
					f.write(str(i))
					f.write(str(j))
					f.write(str(k))
				print(i, j, k)
				print(t:=solve(0, [], m_d))
				if not t:
					m=0
					0/m
			
#gen_moves([0, 1, 1], [])
#solve(0, [], 3)
gen_pos(10)