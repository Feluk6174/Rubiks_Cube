class cube():
    def __init__(self):
        self.pos = [[[[], [], []], [[], [], []], [[], [], []]], [[[], [], []], [[], [], []], [[], [], []]], [[[], [], []], [[], [], []], [[], [], []]]]
        {"type": "edge", "colors":["w", "r"], "rotations": 0}
        {"type": "edge", "colors":["w", "o"], "rotations": 0}
        {"type": "edge", "colors":["w", "g"], "rotations": 0}
        {"type": "edge", "colors":["w", "b"], "rotations": 0}
        self.pos[0][0][1] = {"type": "edge", "colors":["w", "b"], "rotations": 0}
        self.pos[0][1][0] = {"type": "edge", "colors":["w", "o"], "rotations": 0}
        self.pos[0][1][2] = {"type": "edge", "colors":["w", "r"], "rotations": 0}
        self.pos[0][2][1] = {"type": "edge", "colors":["w", "g"], "rotations": 0}
        #self.pos[2]

        