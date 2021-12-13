import cube_3x3, random

def scramble(length, possible_moves):
    cube = cube_3x3.cube()
    for i in range(length):
        cube.move(possible_moves[random.randint(0, len(possible_moves))])