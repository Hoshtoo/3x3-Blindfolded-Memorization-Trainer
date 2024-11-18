from Cube import cube

class main:
    def __init__(self):
        with open('config.txt', 'r') as config:
            self.ALGORITHM_FILE_PATH = config.readline().split('"')[1].strip()
            self.HISTORY_FILE_PATH = config.readline().split('"')[1].strip()
            if 'False' in config.readline().split('--')[1]:
                self.PRINT_CUBE = False
            else:
                self.PRINT_CUBE = True
        self.historyFileExists = False
        if self.HISTORY_FILE_PATH != "":
            self.historyFileExists = True
        else:
            self.history = []
        self.manualAlgorithmInput = True
        if self.ALGORITHM_FILE_PATH != "":
            self.manualAlgorithmInput = False
            with open(self.ALGORITHM_FILE_PATH, 'r') as algorithmFile:
                self.algorithms = algorithmFile.readlines()
            for index in range(len(self.algorithms)):
                self.mainLoop(index)
        else:
            while True:
                if self.mainLoop(-1):
                    break

    def mainLoop(self, algorithmIndex):
        Cube = cube()
        if self.manualAlgorithmInput:
            scramble = input('Enter the scramble seperated by spaces or type exit to quit the program: ') 
            if scramble != 'exit':
                Cube.executeAlg(scramble)
            else:
                return 1    # Exit code to quit program
        else:
            scramble = self.algorithms[algorithmIndex]
            Cube.executeAlg(scramble)

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
        
        cubeCorrect = True
        edgesCorrect = True
        cornersCorrect = True
        if Cube.cube == Cube.startingCube:
            print("CORRECT MEMORIZATION")
        else:
            for x in range(6):
                if not (Cube.cube[x][1] == Cube.cube[x][3] and Cube.cube[x][3] == Cube.cube[x][5] and Cube.cube[x][5] == Cube.cube[x][7] and Cube.cube[x][7] == x):
                    print("Edges were not correct")
                    edgesCorrect = False
                    cubeCorrect = False
                    break
            for x in range(6):
                if not (Cube.cube[x][0] == Cube.cube[x][2] and Cube.cube[x][2] == Cube.cube[x][6] and Cube.cube[x][6] == Cube.cube[x][8] and Cube.cube[x][8] == x):
                    print("Corners were not correct")
                    cornersCorrect = False
                    cubeCorrect = False
                    break
        
        toAppend = ''
        if cubeCorrect:
            toAppend += 'True, True, True'
        elif edgesCorrect:
            toAppend += 'False, True, False'
        elif cornersCorrect:
            toAppend += 'False, False, True'
        else:
            toAppend += 'False, False, False'
            if self.PRINT_CUBE:
                Cube.displayCube()
        toAppend += '\n'

        if self.historyFileExists:
            with open(self.HISTORY_FILE_PATH, 'a') as self.historyFile:
                self.historyFile.write(toAppend)
        else:
            self.history.append(toAppend)
        return 0    # Normal exit code

if __name__ == '__main__':
    main()