import copy

# Programmer: Hoshtoo
# Date: 09.03.2024
# Version: 1.0

class cube:
    def __init__(self):
        self.WHITE = 0
        self.ORANGE = 1
        self.GREEN = 2
        self.RED = 3
        self.BLUE = 4
        self.YELLOW = 5
        colors = [self.WHITE, self.ORANGE, self.GREEN, self.RED, self.BLUE, self.YELLOW]
        self.cube = [[color for _ in range(9)] for color in colors]
        self.startingCube = copy.deepcopy(self.cube)
        self.edgeSetupMoves = {
            'A': ["Lw2 D' L2", "L2 D Lw2"],
            'C': ["Lw2 D L2", "L2 D' Lw2"],
            'D': ["", ""],
            'E': ["L Dw' L", "L' Dw L'"],
            'F': ["Dw' L", "L' Dw"],
            'G': ["L' Dw' L", "L' Dw L"],
            'H': ["Dw L'", "L Dw'"],
            'I': ["Lw D' L2", "L2 D Lw'"],
            'J': ["Dw2 L", "L' Dw2"],
            'K': ["Lw D L2", "L2 D' Lw'"],
            'L': ["L'", "L"],
            'N': ["Dw L", "L' Dw'"],
            'O': ["D2 L' Dw' L", "L' Dw L D2"],
            'P': ["Dw' L'", "L Dw"],
            'Q': ["Lw' D L2", "L2 D' Lw"],
            'R': ["L", "L'"],
            'S': ["Lw' D' L2", "L2 D Lw"],
            'T': ["Dw2 L'", "L Dw2"],
            'U': ["D' L2", "L2 D"],
            'V': ["D2 L2", "L2 D2"],
            'W': ["D L2", "L2 D'"],
            'X': ["L2", "L2"]
        }
        self.cornerSetupMoves = {
            'B': ["R2", "R2"],
            'C': ["F2 D", "D' F2"],
            'D': ["F2", "F2"],
            'F': ["F' D", "D' F"],
            'G': ["F'", "F"],
            'H': ["D' R", "R' D"],
            'I': ["F R'", "R, F'"],
            'J': ["R'", "R"],
            'K': ["F' R'", "R F"],
            'L': ["F2 R'", "R F2"],
            'M': ["F", "F'"],
            'N': ["R' F", "F' R"],
            'O': ["R2 F", "F' R2"],
            'P': ["R F", "F' R'"],
            'Q': ["R D'", "D R'"],
            'S': ["D F'", "F D'"],
            'T': ["R", "R'"],
            'U': ["D", "D'"],
            'V': ["", ""],
            'W': ["D'", "D"],
            'X': ["D2", "D2"]
        }

    def executeAlg(self, alg: str):
        algMoves = alg.split()
        for move in algMoves:
            self.turn(move)

    def displayCube(self):
        print('       ', str(self.cube[0][0]), str(self.cube[0][1]), str(self.cube[0][2]))
        print('       ', str(self.cube[0][3]), str(self.cube[0][4]), str(self.cube[0][5]))
        print('       ', str(self.cube[0][6]), str(self.cube[0][7]), str(self.cube[0][8]))
        print()
        print(str(self.cube[1][0]), str(self.cube[1][1]), str(self.cube[1][2]), ' ', str(self.cube[2][0]), str(self.cube[2][1]), str(self.cube[2][2]), ' ', str(self.cube[3][0]), str(self.cube[3][1]), str(self.cube[3][2]), ' ', str(self.cube[4][0]), str(self.cube[4][1]), str(self.cube[4][2]))
        print(str(self.cube[1][3]), str(self.cube[1][4]), str(self.cube[1][5]), ' ', str(self.cube[2][3]), str(self.cube[2][4]), str(self.cube[2][5]), ' ', str(self.cube[3][3]), str(self.cube[3][4]), str(self.cube[3][5]), ' ', str(self.cube[4][3]), str(self.cube[4][4]), str(self.cube[4][5]))
        print(str(self.cube[1][6]), str(self.cube[1][7]), str(self.cube[1][8]), ' ', str(self.cube[2][6]), str(self.cube[2][7]), str(self.cube[2][8]), ' ', str(self.cube[3][6]), str(self.cube[3][7]), str(self.cube[3][8]), ' ', str(self.cube[4][6]), str(self.cube[4][7]), str(self.cube[4][8]))
        print()
        print('       ', str(self.cube[5][0]), str(self.cube[5][1]), str(self.cube[5][2]))
        print('       ', str(self.cube[5][3]), str(self.cube[5][4]), str(self.cube[5][5]))
        print('       ', str(self.cube[5][6]), str(self.cube[5][7]), str(self.cube[5][8]))
        
    def turn(self, notation):
        if notation == 'R':
            # top right
            placeholder = self.cube[0][2]
            self.cube[0][2] = self.cube[2][2]
            self.cube[2][2] = self.cube[5][2]
            self.cube[5][2] = self.cube[4][6]
            self.cube[4][6] = placeholder
            # middle right
            placeholder = self.cube[0][5]
            self.cube[0][5] = self.cube[2][5]
            self.cube[2][5] = self.cube[5][5]
            self.cube[5][5] = self.cube[4][3]
            self.cube[4][3] = placeholder
            # bottom right
            placeholder = self.cube[0][8]
            self.cube[0][8] = self.cube[2][8]
            self.cube[2][8] = self.cube[5][8]
            self.cube[5][8] = self.cube[4][0]
            self.cube[4][0] = placeholder
            self.rotateFace(3)
        elif notation == 'R2':
            self.turn('R')
            self.turn('R')
        elif notation == "R'":
            self.turn('R')
            self.turn('R')
            self.turn('R')
        elif notation == 'Rw':
            self.turn('R')
            self.turn("M'")
        elif notation == 'Rw2':
            self.turn('R2')
            self.turn('M2')
        elif notation == "Rw'":
            self.turn("R'")
            self.turn('M')
        elif notation == 'L':
            # top left
            placeholder = self.cube[0][0]
            self.cube[0][0] = self.cube[4][8]
            self.cube[4][8] = self.cube[5][0]
            self.cube[5][0] = self.cube[2][0]
            self.cube[2][0] = placeholder
            # middle left
            placeholder = self.cube[0][3]
            self.cube[0][3] = self.cube[4][5]
            self.cube[4][5] = self.cube[5][3]
            self.cube[5][3] = self.cube[2][3]
            self.cube[2][3] = placeholder
            # bottom left
            placeholder = self.cube[0][6]
            self.cube[0][6] = self.cube[4][0]
            self.cube[4][0] = self.cube[5][6]
            self.cube[5][6] = self.cube[2][6]
            self.cube[2][6] = placeholder
            self.rotateFace(1)
        elif notation == 'L2':
            self.turn('L')
            self.turn('L')
        elif notation == "L'":
            self.turn('L')
            self.turn('L')
            self.turn('L')
        elif notation == 'Lw':
            self.turn('L')
            self.turn('M')
        elif notation == 'Lw2':
            self.turn('L2')
            self.turn('M2')
        elif notation == "Lw'":
            self.turn("L'")
            self.turn("M'")
        elif notation == 'U':
            # left top
            placeholder = self.cube[2][0]
            self.cube[2][0] = self.cube[3][0]
            self.cube[3][0] = self.cube[4][0]
            self.cube[4][0] = self.cube[1][0]
            self.cube[1][0] = placeholder
            # middle top
            placeholder = self.cube[2][1]
            self.cube[2][1] = self.cube[3][1]
            self.cube[3][1] = self.cube[4][1]
            self.cube[4][1] = self.cube[1][1]
            self.cube[1][1] = placeholder
            # right top
            placeholder = self.cube[2][2]
            self.cube[2][2] = self.cube[3][2]
            self.cube[3][2] = self.cube[4][2]
            self.cube[4][2] = self.cube[1][2]
            self.cube[1][2] = placeholder
            self.rotateFace(0)
        elif notation == 'U2':
            self.turn('U')
            self.turn('U')
        elif notation == "U'":
            self.turn('U')
            self.turn('U')
            self.turn('U')
        elif notation == 'Uw':
            self.turn('U')
            self.turn("E'")
        elif notation == 'Uw2':
            self.turn('U2')
            self.turn('E2')
        elif notation == "Uw'":
            self.turn("U'")
            self.turn('E')
        elif notation == 'D':
            # left bottom
            placeholder = self.cube[2][6]
            self.cube[2][6] = self.cube[1][6]
            self.cube[1][6] = self.cube[4][6]
            self.cube[4][6] = self.cube[3][6]
            self.cube[3][6] = placeholder
            # middle bottom
            placeholder = self.cube[2][7]
            self.cube[2][7] = self.cube[1][7]
            self.cube[1][7] = self.cube[4][7]
            self.cube[4][7] = self.cube[3][7]
            self.cube[3][7] = placeholder
            # right bottom
            placeholder = self.cube[2][8]
            self.cube[2][8] = self.cube[1][8]
            self.cube[1][8] = self.cube[4][8]
            self.cube[4][8] = self.cube[3][8]
            self.cube[3][8] = placeholder
            self.rotateFace(5)
        elif notation == 'D2':
            self.turn('D')
            self.turn('D')
        elif notation == "D'":
            self.turn('D')
            self.turn('D')
            self.turn('D')
        elif notation == 'Dw':
            self.turn('D')
            self.turn('E')
        elif notation == 'Dw2':
            self.turn('D2')
            self.turn('E2')
        elif notation == "Dw'":
            self.turn("D'")
            self.turn("E'")
        elif notation == 'F':
            # left corner
            placeholder = self.cube[0][6]
            self.cube[0][6] = self.cube[1][8]
            self.cube[1][8] = self.cube[5][2]
            self.cube[5][2] = self.cube[3][0]
            self.cube[3][0] = placeholder
            # edges
            placeholder = self.cube[0][7]
            self.cube[0][7] = self.cube[1][5]
            self.cube[1][5] = self.cube[5][1]
            self.cube[5][1] = self.cube[3][3]
            self.cube[3][3] = placeholder
            # right corner
            placeholder = self.cube[0][8]
            self.cube[0][8] = self.cube[1][2]
            self.cube[1][2] = self.cube[5][0]
            self.cube[5][0] = self.cube[3][6]
            self.cube[3][6] = placeholder
            self.rotateFace(2)
        elif notation == 'F2':
            self.turn('F')
            self.turn('F')
        elif notation == "F'":
            self.turn('F')
            self.turn('F')
            self.turn('F')
        elif notation == 'Fw':
            self.turn('F')
            self.turn('S')
        elif notation == 'Fw2':
            self.turn('F2')
            self.turn('S2')
        elif notation == "Fw'":
            self.turn("F'")
            self.turn("S'")
        elif notation == 'B':
            # left corner
            placeholder = self.cube[0][0]
            self.cube[0][0] = self.cube[3][2]
            self.cube[3][2] = self.cube[5][8]
            self.cube[5][8] = self.cube[1][6]
            self.cube[1][6] = placeholder
            # middle edge
            placeholder = self.cube[0][1]
            self.cube[0][1] = self.cube[3][5]
            self.cube[3][5] = self.cube[5][7]
            self.cube[5][7] = self.cube[1][3]
            self.cube[1][3] = placeholder
            # right corner
            placeholder = self.cube[0][2]
            self.cube[0][2] = self.cube[3][8]
            self.cube[3][8] = self.cube[5][6]
            self.cube[5][6] = self.cube[1][0]
            self.cube[1][0] = placeholder
            self.rotateFace(4)
        elif notation == 'B2':
            self.turn('B')
            self.turn('B')
        elif notation == "B'":
            self.turn('B')
            self.turn('B')
            self.turn('B')
        elif notation == 'Bw':
            self.turn('B')
            self.turn("S'")
        elif notation == 'Bw2':
            self.turn('B2')
            self.turn('S2')
        elif notation == "Bw'":
            self.turn("B'")
            self.turn('S')
        elif notation == 'M':
            # top left
            placeholder = self.cube[0][1]
            self.cube[0][1] = self.cube[4][7]
            self.cube[4][7] = self.cube[5][1]
            self.cube[5][1] = self.cube[2][1]
            self.cube[2][1] = placeholder
            # middle left
            placeholder = self.cube[0][4]
            self.cube[0][4] = self.cube[4][4]
            self.cube[4][4] = self.cube[5][4]
            self.cube[5][4] = self.cube[2][4]
            self.cube[2][4] = placeholder
            # bottom left
            placeholder = self.cube[0][7]
            self.cube[0][7] = self.cube[4][1]
            self.cube[4][1] = self.cube[5][7]
            self.cube[5][7] = self.cube[2][7]
            self.cube[2][7] = placeholder
        elif notation == 'M2':
            self.turn('M')
            self.turn('M')
        elif notation == "M'":
            self.turn('M')
            self.turn('M')
            self.turn('M')
        elif notation == 'E':
            # left edge
            placeholder = self.cube[2][3]
            self.cube[2][3] = self.cube[1][3]
            self.cube[1][3] = self.cube[4][3]
            self.cube[4][3] = self.cube[3][3]
            self.cube[3][3] = placeholder
            # center
            placeholder = self.cube[2][4]
            self.cube[2][4] = self.cube[1][4]
            self.cube[1][4] = self.cube[4][4]
            self.cube[4][4] = self.cube[3][4]
            self.cube[3][4] = placeholder
            # right edge
            placeholder = self.cube[2][5]
            self.cube[2][5] = self.cube[1][5]
            self.cube[1][5] = self.cube[4][5]
            self.cube[4][5] = self.cube[3][5]
            self.cube[3][5] = placeholder
        elif notation == 'E2':
            self.turn('E')
            self.turn('E')
        elif notation == "E'":
            self.turn('E')
            self.turn('E')
            self.turn('E')
        elif notation == 'S':
            # left corner
            placeholder = self.cube[0][3]
            self.cube[0][3] = self.cube[1][7]
            self.cube[1][7] = self.cube[5][5]
            self.cube[5][5] = self.cube[3][1]
            self.cube[3][1] = placeholder
            # edges
            placeholder = self.cube[0][4]
            self.cube[0][4] = self.cube[1][4]
            self.cube[1][4] = self.cube[5][4]
            self.cube[5][4] = self.cube[3][4]
            self.cube[3][4] = placeholder
            # right corner
            placeholder = self.cube[0][5]
            self.cube[0][5] = self.cube[1][1]
            self.cube[1][1] = self.cube[5][3]
            self.cube[5][3] = self.cube[3][7]
            self.cube[3][7] = placeholder
        elif notation == 'S2':
            self.turn('S')
            self.turn('S')
        elif notation == "S'":
            self.turn('S')
            self.turn('S')
            self.turn('S')
        elif notation == 'x':
            self.turn('R')
            self.turn("M'")
            self.turn("L'")
        elif notation == 'x2':
            self.turn('R2')
            self.turn('M2')
            self.turn('L2')
        elif notation == "x'":
            self.turn("R'")
            self.turn('M')
            self.turn('L')
        elif notation == 'y':
            self.turn('U')
            self.turn("E'")
            self.turn("D'")
        elif notation == 'y2':
            self.turn('U2')
            self.turn('E2')
            self.turn('D2')
        elif notation == "y'":
            self.turn("U'")
            self.turn('E')
            self.turn('D')
        elif notation == 'z':
            self.turn('F')
            self.turn('S')
            self.turn("B'")
        elif notation == 'z2':
            self.turn('F2')
            self.turn('S2')
            self.turn('B2')
        elif notation == "z'":
            self.turn("F'")
            self.turn("S'")
            self.turn('B')
    def rotateFace(self, face):
        # corner rotate
        placeholder = self.cube[face][0]
        self.cube[face][0] = self.cube[face][6]
        self.cube[face][6] = self.cube[face][8]
        self.cube[face][8] = self.cube[face][2]
        self.cube[face][2] = placeholder
        # edge rotate
        placeholder = self.cube[face][1]
        self.cube[face][1] = self.cube[face][3]
        self.cube[face][3] = self.cube[face][7]
        self.cube[face][7] = self.cube[face][5]
        self.cube[face][5] = placeholder

Cube = cube()
Cube.executeAlg(input('Enter the scramble seperated by spaces: '))

for letter in (input('Enter the edge memorization seperated by spaces: ').split()):
    for x in range(len(letter)):
        Cube.executeAlg(Cube.edgeSetupMoves[letter[x]][0])
        Cube.executeAlg("R U R' U' R' F R2 U' R' U' R U R' F'")
        Cube.executeAlg(Cube.edgeSetupMoves[letter[x]][1])

if (input('If there is parity, type y: ') == 'y'):
    Cube.executeAlg("R U' R' U' R U R D R' U' R D' R' U2 R'")

for letter in (input('Enter the corner memorization seperated by spaces: ').split()):
    for x in range(len(letter)):
        try:
            Cube.executeAlg(Cube.cornerSetupMoves[letter[x]][0])
            Cube.executeAlg("R U' R' U' R U R' F' R U R' U' R' F R")
            Cube.executeAlg(Cube.cornerSetupMoves[letter[x]][1])
        except:
            pass

if Cube.cube == Cube.startingCube:
    print("CORRECT MEMORIZATION")
else:
    for x in range(6):
        if not (Cube.cube[x][1] == Cube.cube[x][3] and Cube.cube[x][3] == Cube.cube[x][5] and Cube.cube[x][5] == Cube.cube[x][7] and Cube.cube[x][7] == x):
            print("Edges were not correct")
            break
    for x in range(6):
        if not (Cube.cube[x][0] == Cube.cube[x][2] and Cube.cube[x][2] == Cube.cube[x][6] and Cube.cube[x][6] == Cube.cube[x][8] and Cube.cube[x][8] == x):
            print("Corners were not correct")
            break
