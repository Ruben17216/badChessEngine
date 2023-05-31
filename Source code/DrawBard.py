class Board:
    def __init__(self, Players):
        self.BoardColumn = 8
        self.BoardRow = 8
        self.PlayerWhite = Players[0]
        self.PlayerBack = Players[1]

    def draw(self, Players):
        bored = []
        for i in range(8):
            boredR = []
            for I in range(8):
                PiceDrawnB = False; PiceDrawnW = False
                for obj in Players[0]:
                    if obj.CPos == I+1 and obj.RPos == i+1:
                        PiceDrawnW = True
                        PiceToDraw = obj.Type[0]
                        if obj.Type == "Knight":
                            PiceToDraw = "N"
                        if obj.Type == "King":
                            KingLowcationRowWhite = i+1
                            KingLowcationColumnWhite = I+1
                        if obj.Type == ".PasontDot":
                            if obj.MoveCount > 0:
                                obj.RPos= 9; obj.CPos= 9
                            if obj.MoveCount == 0:
                                obj.MoveCount = obj.MoveCount + 1
                        boredR.append(PiceToDraw)
                    elif PiceDrawnB == False and PiceDrawnW == False:
                        PiceDrawnW = False
                for obj in Players[1]:
                    if obj.CPos == I+1 and obj.RPos == i+1:
                        PiceDrawnB = True
                        PiceToDraw = obj.Type[0]
                        PiceToDraw = PiceToDraw.lower()
                        if obj.Type == "Knight":
                            PiceToDraw = "n"
                        if obj.Type == "King":
                            KingLowcationRowBlack = i+1
                            KingLowcationColumnBlack = I+1
                        if obj.Type == ".PasontDot":
                            if obj.MoveCount > 0:
                                obj.RPos = 9; obj.CPos = 9
                            if obj.MoveCount == 0:
                                obj.MoveCount = obj.MoveCount + 1
                        boredR.append(PiceToDraw)
                    elif PiceDrawnB == False and PiceDrawnW == False:
                        PiceDrawnB = False
                if PiceDrawnW == False and PiceDrawnB == False:
                    boredR.append(" ")
            bored.append(boredR)
        print("    A   B   C   D   E   F   G   H   ")
        i = 0
        number = 9
        for item in bored:
            line = []
            number = number - 1
            I = number
            I = str(I)
            start = [I, " ┃ "]
            start = "".join(start)
            line.append(str(start))
            for element in item:
                line.append(str(element))
                line.append(str(" ┃ "))
            i = i + 1
            if i == 1:
                print("  ┏━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┓")
            print("".join(line))
            if i == 8:
                print("  ┗━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┛")

            elif i != 8 or i != 1:
                print("  ┣━━━╋━━━╋━━━╋━━━╋━━━╋━━━╋━━━╋━━━┫")
        print()
        return KingLowcationRowWhite, KingLowcationColumnWhite, KingLowcationRowBlack, KingLowcationColumnBlack