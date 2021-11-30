import cube_3x3, solve_state_0, solve_state_1, solve_state_2, solve_state_3

scrmble = input("Input scramble: ")

if scrmble == "a":
    cube = cube_3x3.cube()
    cube.scramble()
    scrmble = cube.get_state()
    print(scrmble)

solve_0 = solve_state_0.solve(scrmble)
solve_1 = solve_state_1.solve(solve_0[1])
solve_2 = solve_state_2.solve(solve_1[1])
solve_3 = solve_state_3.solve(solve_2[1])

print(solve_0)
print(solve_1)
print(solve_2)
print(solve_3)
print(solve_0+solve_1+solve_2+solve_3)
