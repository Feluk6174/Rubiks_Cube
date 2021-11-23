import cube_3x3

solve=0
RL_block=0
RLFB_block=0
RLFBUD_block=0

cube=cube_3x3.cube()

cube
print (cube)

if cube.cube["w"]["edge"].count("w")==4 and cube.cube["w"]["corner"].count("w")==4:
    if cube.cube["g"]["edge"].count("g")==4 and cube.cube["g"]["corner"].count("g")==4:
        if cube.cube["y"]["edge"].count("y")==4 and cube.cube["y"]["corner"].count("y")==4:
            if cube.cube["o"]["edge"].count("o")==4 and cube.cube["o"]["corner"].count("o")==4:
                if cube.cube["r"]["edge"].count("r")==4 and cube.cube["r"]["corner"].count("r")==4:
                    if cube.cube["b"]["edge"].count("b")==4 and cube.cube["b"]["corner"].count("b")==4:
                        solve=1
                        print (solve)

if cube.cube["w"]["edge"].count("b")==0:
    if cube.cube["y"]["edge"].count("b")==0:
        if cube.cube["w"]["edge"].count("g")==0:
            if cube.cube["y"]["edge"].count("g")==0:
                if cube.cube["o"]["edge"][0]!=("w"):
                    if cube.cube["o"]["edge"][2]!=("w"):
                        if cube.cube["o"]["edge"][0]!=("y"):
                            if cube.cube["o"]["edge"][2]!=("y"):
                                if cube.cube["r"]["edge"][0]!=("w"):
                                    if cube.cube["r"]["edge"][2]!=("w"):
                                        if cube.cube["r"]["edge"][0]!=("y"):
                                            if cube.cube["r"]["edge"][2]!=("y"):
                                                if cube.cube["o"]["edge"][1]!=("g"):
                                                    if cube.cube["o"]["edge"][3]!=("g"):
                                                        if cube.cube["o"]["edge"][1]!=("b"):
                                                            if cube.cube["o"]["edge"][3]!=("b"):
                                                                if cube.cube["r"]["edge"][1]!=("g"):
                                                                    if cube.cube["r"]["edge"][3]!=("g"):
                                                                        if cube.cube["r"]["edge"][1]!=("b"):
                                                                            if cube.cube["r"]["edge"][3]!=("b"):
                                                                                RL_block=1
                                                                                print (RL_block)

if cube.cube["w"]["edge"].count("w")+cube.cube["w"]["edge"].count("y")==4:
    if cube.cube["y"]["edge"].count("w")+cube.cube["y"]["edge"].count("y")==4:
        if cube.cube["g"]["edge"][1]==("b") or cube.cube["g"]["edge"][1]!=("g"):
            if cube.cube["g"]["edge"][3]==("b") or cube.cube["3"]["edge"][1]!=("g"):
                if cube.cube["b"]["edge"][1]==("b") or cube.cube["b"]["edge"][1]!=("g"):
                    if cube.cube["b"]["edge"][3]==("b") or cube.cube["b"]["edge"][3]!=("g"):
                        if cube.cube["w"]["corner"].count("w")+cube.cube["w"]["corner"].count("y")==4:
                            if cube.cube["y"]["corner"].count("w")+cube.cube["y"]["corner"].count("y")==4:
                                RLFB_block=1
                                print (RLFB_block)

if cube.cube["w"]["edge"].count("w")+cube.cube["w"]["edge"].count("y")==4:
    if cube.cube["y"]["edge"].count("w")+cube.cube["y"]["edge"].count("y")==4:
        if cube.cube["b"]["edge"].count("b")+cube.cube["b"]["edge"].count("g")==4:
            if cube.cube["g"]["edge"].count("b")+cube.cube["g"]["edge"].count("g")==4:
                if cube.cube["r"]["edge"].count("r")+cube.cube["r"]["edge"].count("o")==4:
                    if cube.cube["o"]["edge"].count("r")+cube.cube["o"]["edge"].count("o")==4:
                        if cube.cube["w"]["corner"].count("w")+cube.cube["w"]["corner"].count("y")==4:
                            if cube.cube["y"]["corner"].count("w")+cube.cube["y"]["corner"].count("y")==4:
                                if cube.cube["b"]["corner"].count("b")+cube.cube["b"]["corner"].count("g")==4:
                                    if cube.cube["g"]["corner"].count("b")+cube.cube["g"]["corner"].count("g")==4:
                                        if cube.cube["r"]["corner"].count("r")+cube.cube["r"]["corner"].count("o")==4:
                                            if cube.cube["o"]["corner"].count("r")+cube.cube["o"]["corner"].count("o")==4:
                                                RLFBUD_block=1
                                                print (RLFBUD_block)
