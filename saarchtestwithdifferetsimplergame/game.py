import random

class game():
    def __init__(self, pos=[]):
        if not len(pos) == 3:
            self.scramble()
        else:
            self.pos = pos

    def __str__(self):
        return str(self.pos)

    def mov1(self):
        if not self.pos[0] == 9:
            self.pos[0] += 1
        else:
            self.pos[0] = 0

    def mov2(self):
        if not self.pos[0] == 0:
            self.pos[0] -= 1
        else:
            self.pos[0] = 9
        
        if not self.pos[1] == 9:
            self.pos[1] += 1
        else:
            self.pos[1] = 0
        
        if not self.pos[2] == 0:
            self.pos[2] -= 1
        else:
            self.pos[2] = 9

    def mov3(self):
        if not self.pos[2] == 9:
            self.pos[2] += 1
        else:
            self.pos[2] = 0

    def move(self, x):
        
        if x == 0:
            self.mov1()

        elif x == 1:
            self.mov2()
        
        elif x == 2:
            self.mov3()

    def scramble(self):
        self.pos = [random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)]

    def solved(self):
        return (self.pos[0] == self.pos[1]) and (self.pos[0] == self.pos[2])

def player_solve():
    g = game([3, 2, 1])

    while not g.solved():
        print(g)
        x = int(input("move: "))
        g.move(x)

    print(g)


#player_solve()
#[1, 0, 1, 2, 2], [1, 0, 1, 0, 2], [0, 0, 0, 0, 0, 0, 1, 0, 2, 2] [0, 0, 0, 0, 0, 0, 1, 0, 2, 2]