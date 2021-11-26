import cube_3x3
			
		
			
cub = cube_3x3.cube()



while True:
	print(cub)
	x = input("	>> ")
	if x == "e":
		print(cub.get_state())
		break
	elif x == "s":
		cub.scramble()
	else:
		cub.move(x)