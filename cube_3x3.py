import random

class cube():
	def __init__(self):
    	#inittzialises the cube instance, crating a cube, the possition of the cube is stored in a
		#dictionary, the dict contains a dictionary for  each face. Those dictionaries contain a dictioany
		#each, in that dictionary there are 2 arrays, eaach conttaining a a color of a sticker.
		# the sikers are sorted clockwaise starting form the top one:
		# 0 0 1
		# 3 - 1
		# 3 2 2

		self.colors = ["o", "w", "r", "y", "g", "b"]
		self.colors_in_order = ["w", "g", "r", "b", "o", "y"]
		self.cube = {}
		for color in self.colors:
			self.cube[color] = {}
			self.cube[color]["edge"] = [color for i in range(4)]
			self.cube[color]["corner"] = [color for i in range(4)]
			
		self.moves = ["u", "u'", "u2", "r", "r'", "r2", "l", "l'", "l2", "d", "d'", "d2", "f", "f'", "f2", "b", "b'", "b2"]
			
			
	def __str__(self):
    	# returns a strinng with the current possition of the cube, looks like tht:
		#       b b b
		#	    b b b
		#	    b b b
		# o o o w w w r r r y y y 
		# o o o w w w r r r y y y
		# o o o w w w r r r y y y
		#	    g g g
		#	    g g g
		#	    g g g
		return f"""      {self.cube["b"]["corner"][2]} {self.cube["b"]["edge"][2]} {self.cube["b"]["corner"][3]}
      {self.cube["b"]["edge"][1]} b {self.cube["b"]["edge"][3]}
      {self.cube["b"]["corner"][1]} {self.cube["b"]["edge"][0]} {self.cube["b"]["corner"][0]}
{self.cube["o"]["corner"][3]} {self.cube["o"]["edge"][3]} {self.cube["o"]["corner"][0]} {self.cube["w"]["corner"][0]} {self.cube["w"]["edge"][0]} {self.cube["w"]["corner"][1]} {self.cube["r"]["corner"][1]} {self.cube["r"]["edge"][1]} {self.cube["r"]["corner"][2]} {self.cube["y"]["corner"][2]} {self.cube["y"]["edge"][2]} {self.cube["y"]["corner"][3]} 
{self.cube["o"]["edge"][2]} o {self.cube["o"]["edge"][0]} {self.cube["w"]["edge"][3]} w {self.cube["w"]["edge"][1]} {self.cube["r"]["edge"][0]} r {self.cube["r"]["edge"][2]} {self.cube["y"]["edge"][1]} y {self.cube["y"]["edge"][3]}
{self.cube["o"]["corner"][2]} {self.cube["o"]["edge"][1]} {self.cube["o"]["corner"][1]} {self.cube["w"]["corner"][3]} {self.cube["w"]["edge"][2]} {self.cube["w"]["corner"][2]} {self.cube["r"]["corner"][0]} {self.cube["r"]["edge"][3]} {self.cube["r"]["corner"][3]} {self.cube["y"]["corner"][1]} {self.cube["y"]["edge"][0]} {self.cube["y"]["corner"][0]} 
      {self.cube["g"]["corner"][0]} {self.cube["g"]["edge"][0]} {self.cube["g"]["corner"][1]}
      {self.cube["g"]["edge"][3]} g {self.cube["g"]["edge"][1]}
      {self.cube["g"]["corner"][3]} {self.cube["g"]["edge"][2]} {self.cube["g"]["corner"][2]}
      """
			
	def turn_face(self, face:str):
    	#moves the stikes of the face. and not the stikeron the side
		self.cube[face]["edge"] = [self.cube[face]["edge"][3], self.cube[face]["edge"][0], self.cube[face]["edge"][1], self.cube[face]["edge"][2]]
		self.cube[face]["corner"] = [self.cube[face]["corner"][3], self.cube[face]["corner"][0], self.cube[face]["corner"][1], self.cube[face]["corner"][2]]
							
							
	def turn_side(self, face:str, info:list):
    	#turns the entire face including the side stiker
		self.turn_face(face)
		
		#stores temprarly the values of the stiker thatmove on two oposite faces
		temp1 = [self.cube[info[0]["color"]]["corner"][info[0]["nums"][0]], self.cube[info[0]["color"]]["edge"][info[0]["nums"][1]], self.cube[info[0]["color"]]["corner"][info[0]["nums"][2]]]
		
		temp2 = [self.cube[info[2]["color"]]["corner"][info[2]["nums"][0]], self.cube[info[2]["color"]]["edge"][info[2]["nums"][1]], self.cube[info[2]["color"]]["corner"][info[2]["nums"][2]]]
		
		#owerwites the value of the stored faces with the ieces that go there
		self.cube[info[0]["color"]]["corner"][info[0]["nums"][0]] = self.cube[info[3]["color"]]["corner"][info[3]["nums"][0]]
		self.cube[info[0]["color"]]["edge"][info[0]["nums"][1]] = self.cube[info[3]["color"]]["edge"][info[3]["nums"][1]]
		self.cube[info[0]["color"]]["corner"][info[0]["nums"][2]] = self.cube[info[3]["color"]]["corner"][info[3]["nums"][2]]
		
		self.cube[info[2]["color"]]["corner"][info[2]["nums"][0]] = self.cube[info[1]["color"]]["corner"][info[1]["nums"][0]]
		self.cube[info[2]["color"]]["edge"][info[2]["nums"][1]] = self.cube[info[1]["color"]]["edge"][info[1]["nums"][1]]
		self.cube[info[2]["color"]]["corner"][info[2]["nums"][2]] = self.cube[info[1]["color"]]["corner"][info[1]["nums"][2]]
		
		#overites the values oth the faces not stored, with the stored values
		self.cube[info[1]["color"]]["corner"][info[1]["nums"][0]] = temp1[0]
		self.cube[info[1]["color"]]["edge"][info[1]["nums"][1]] = temp1[1]
		self.cube[info[1]["color"]]["corner"][info[1]["nums"][2]] = temp1[2]
		
		self.cube[info[3]["color"]]["corner"][info[3]["nums"][0]] = temp2[0]
		self.cube[info[3]["color"]]["edge"][info[3]["nums"][1]] = temp2[1]
		self.cube[info[3]["color"]]["corner"][info[3]["nums"][2]] = temp2[2]
		
	#The next 6 functions (u, d, l, r, f, b) call the turn side function with the nessesary data
	def u(self):
		d = [{"color": "g", "nums": [0, 0, 1]}, {"color": "o", "nums": [0, 0, 1]}, {"color": "b", "nums": [0, 0, 1]}, {"color": "r", "nums": [0, 0, 1]}, ]
		
		self.turn_side("w", d)
		
		
	def f(self):
		d = [{"color": "w", "nums": [3, 2, 2]}, {"color": "r", "nums": [0, 3, 3]}, {"color": "y", "nums": [1, 0, 0]}, {"color": "o", "nums": [2, 1, 1]}, ]
		
		self.turn_side("g", d)
		
		
	def r(self):
		d = [{"color": "w", "nums": [2, 1, 1]}, {"color": "b", "nums": [0, 3, 3]}, {"color": "y", "nums": [2, 1, 1]}, {"color": "g", "nums": [2, 1, 1]}, ]
		
		self.turn_side("r", d)
		
	
	def d(self):
		d = [{"color": "g", "nums": [3, 2, 2]}, {"color": "r", "nums": [3, 2, 2]}, {"color": "b", "nums": [3, 2, 2]}, {"color": "o", "nums": [3, 2, 2]}, ]
		
		self.turn_side("y", d)
		

	def l(self):
		d = [{"color": "w", "nums": [0, 3, 3]}, {"color": "g", "nums": [0, 3, 3]}, {"color": "y", "nums": [0, 3, 3]}, {"color": "b", "nums": [2, 1, 1]}, ]
		
		self.turn_side("o", d)
		
		
	def b(self):
		d = [{"color": "w", "nums": [0, 0, 1]}, {"color": "o", "nums": [0, 3, 3]}, {"color": "y", "nums": [3, 2, 2]}, {"color": "r", "nums": [2, 1, 1]}, ]
		
		self.turn_side("b", d)

	
	def move(self, move):
    	#This function calls the function of the corresponden face, ih a variable that gets passed, iths the recomended function to acces
		if move == "u":
			self.u()
		if move == "u'":
			self.u()
			self.u()
			self.u()
		if move == "u2":
			self.u()
			self.u()
		
		if move == "f":
			self.f()
		if move == "f'":
			self.f()
			self.f()
			self.f()
		if move == "f2":
			self.f()
			self.f()
			
		if move == "r":
			self.r()
		if move == "r'":
			self.r()
			self.r()
			self.r()
		if move == "r2":
			self.r()
			self.r()
			
		if move == "l":
			self.l()
		if move == "l'":
			self.l()
			self.l()
			self.l()
		if move == "l2":
			self.l()
			self.l()
		
		if move == "d":
			self.d()
		if move == "d'":
			self.d()
			self.d()
			self.d()
		if move == "d2":
			self.d()
			self.d()
		
		if move == "b":
			self.b()
		if move == "b'":
			self.b()
			self.b()
			self.b()
		if move == "b2":
			self.b()
			self.b()

	def scramble(self, scramble:str=""):
		if scramble != "":
			for i, color in enumerate(self.colors_in_order):
				self.cube[color] = {"corner": [scramble[i*9+0], scramble[i*9+2], scramble[i*9+8], scramble[i*9+6]], "edge": [scramble[i*9+1], scramble[i*9+5], scramble[i*9+7], scramble[i*9+3]]}
		else:
			for i in range(40):
				x = random.randint(0,17)
				self.move(self.moves[x])


	def get_state(self):
		scramble = ""
		for i, color in enumerate(self.colors_in_order):
			scramble += self.cube[color]["corner"][0]
			scramble += self.cube[color]["edge"][0]
			scramble += self.cube[color]["corner"][1]
			scramble += self.cube[color]["edge"][3]
			scramble += color
			scramble += self.cube[color]["edge"][1]
			scramble += self.cube[color]["corner"][3]
			scramble += self.cube[color]["edge"][2]
			scramble += self.cube[color]["corner"][2]
		return scramble







	def solved_0(self):
		if self.cube["w"]["edge"].count("b")==0:
			if self.cube["y"]["edge"].count("b")==0:
				if self.cube["w"]["edge"].count("g")==0:
					if self.cube["y"]["edge"].count("g")==0:
						if self.cube["o"]["edge"][0]!=("w"):
							if self.cube["o"]["edge"][2]!=("w"):
								if self.cube["o"]["edge"][0]!=("y"):
									if self.cube["o"]["edge"][2]!=("y"):
										if self.cube["r"]["edge"][0]!=("w"):
											if self.cube["r"]["edge"][2]!=("w"):
												if self.cube["r"]["edge"][0]!=("y"):
													if self.cube["r"]["edge"][2]!=("y"):
														if self.cube["o"]["edge"][1]!=("g"):
															if self.cube["o"]["edge"][3]!=("g"):
																if self.cube["o"]["edge"][1]!=("b"):
																	if self.cube["o"]["edge"][3]!=("b"):
																		if self.cube["r"]["edge"][1]!=("g"):
																			if self.cube["r"]["edge"][3]!=("g"):
																				if self.cube["r"]["edge"][1]!=("b"):
																					if self.cube["r"]["edge"][3]!=("b"):
																						return True
					return False

	def solved_1(self):
		if self.cube["w"]["edge"].count("w")+self.cube["w"]["edge"].count("y")==4:
			if self.cube["y"]["edge"].count("w")+self.cube["y"]["edge"].count("y")==4:
				if self.cube["g"]["edge"][1]==("b") or self.cube["g"]["edge"][1]==("g"):
					if self.cube["g"]["edge"][3]==("b") or self.cube["g"]["edge"][1]==("g"):
						if self.cube["b"]["edge"][1]==("b") or self.cube["b"]["edge"][1]==("g"):
							if self.cube["b"]["edge"][3]==("b") or self.cube["b"]["edge"][3]==("g"):
								return True
		return False

	def solved_2(self):
		if self.cube["w"]["edge"].count("w")+self.cube["w"]["edge"].count("y")==4:
			if self.cube["y"]["edge"].count("w")+self.cube["y"]["edge"].count("y")==4:
				if self.cube["b"]["edge"].count("b")+self.cube["b"]["edge"].count("g")==4:
					if self.cube["g"]["edge"].count("b")+self.cube["g"]["edge"].count("g")==4:
						if self.cube["r"]["edge"].count("r")+self.cube["r"]["edge"].count("o")==4:
							if self.cube["o"]["edge"].count("r")+self.cube["o"]["edge"].count("o")==4:
								if self.cube["w"]["corner"].count("w")+self.cube["w"]["corner"].count("y")==4:
									if self.cube["y"]["corner"].count("w")+self.cube["y"]["corner"].count("y")==4:
										if self.cube["b"]["corner"].count("b")+self.cube["b"]["corner"].count("g")==4:
											if self.cube["g"]["corner"].count("b")+self.cube["g"]["corner"].count("g")==4:
												if self.cube["r"]["corner"].count("r")+self.cube["r"]["corner"].count("o")==4:
													if self.cube["o"]["corner"].count("r")+self.cube["o"]["corner"].count("o")==4:
														return True
		return False
	
	def solved_3(self):
		if self.cube["w"]["edge"].count("w") == 4 and self.cube["w"]["corner"].count("w") == 4:
			if self.cube["g"]["edge"].count("g") ==4 and self.cube["g"]["corner"].count("g") == 4:
				if self.cube["y"]["edge"].count("y")==4 and self.cube["y"]["corner"].count("y")==4:
					if self.cube["o"]["edge"].count("o")==4 and self.cube["o"]["corner"].count("o")==4:
						if self.cube["r"]["edge"].count("r")==4 and self.cube["r"]["corner"].count("r")==4:
							if self.cube["b"]["edge"].count("b")==4 and self.cube["b"]["corner"].count("b")==4:
								return True
		return False