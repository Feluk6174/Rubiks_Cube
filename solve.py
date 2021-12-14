import cProfile 

def main():
    import cube_3x3, solve_state_0, solve_state_1, solve_state_2, solve_state_3

    scramble = input("Input scramble: ")

    if scramble == "a":
        cube = cube_3x3.cube()
        cube.scramble()
        scramble = cube.get_state()
        print(scramble)

    if len(scramble) == 54 and scramble.count("w") == 9 and scramble.count("y") == 9 and scramble.count("g") == 9 and scramble.count("b") == 9 and scramble.count("r") == 9 and scramble.count("o") == 9:
        solve_0 = solve_state_0.solve(scramble)
        solve_1 = solve_state_1.solve(solve_0[1])
        solve_2 = solve_state_2.solve(solve_1[1])
        solve_3 = solve_state_3.solve(solve_2[1])

        print(solve_0)
        print(solve_1)
        print(solve_2)
        print(solve_3)
        print(solve_0+solve_1+solve_2+solve_3)

    else:
        if not len(scramble) == 54:
            extra = "incorrect length"
        else:
            extra = "impossible colors"
        print("Incorrect scramble: "+extra)

if __name__ == "__main__":
    cProfile.run("main()")
