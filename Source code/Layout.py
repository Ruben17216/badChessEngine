from Pieces import *

class layout:
    def default():
        PlayerWhite = []
        PlayerBlack = []
        for i in range(8):
            PlayerBlack.append(Pawn(Type="Pawn" , Player="Black", CPos=i+1, RPos=2, MoveCount=0))
            PlayerWhite.append(Pawn(Type="Pawn", Player="White", CPos=i+1, RPos=7, MoveCount=0))
        for i in range(2):
            I = 2; B = 3
            if i > 0:
                i = 7; I = 7; B = 6
            PlayerBlack.append(Rook(Type="Rook", Player="Black", CPos=i+1, RPos=1, MoveCount=0))
            PlayerWhite.append(Rook(Type="Rook", Player="White", CPos=i+1, RPos=8, MoveCount=0))
            PlayerBlack.append(Knight(Type="Knight", Player="Black", CPos=I, RPos=1, MoveCount=0))
            PlayerWhite.append(Knight(Type="Knight", Player="White", CPos=I, RPos=8, MoveCount=0))
            PlayerBlack.append(Bishop(Type="Bishop", Player="Black", CPos=B, RPos=1, MoveCount=0))
            PlayerWhite.append(Bishop(Type="Bishop", Player="White", CPos=B, RPos=8, MoveCount=0))
        PlayerBlack.append(Queen(Type="Queen", Player="Black", CPos=4, RPos=1, MoveCount=0))
        PlayerWhite.append(Queen(Type="Queen", Player="White", CPos=4, RPos=8, MoveCount=0))
        PlayerBlack.append(King(Type="King", Player="Black", CPos=5, RPos=1, MoveCount=0))
        PlayerWhite.append(King(Type="King", Player="White", CPos=5, RPos=8, MoveCount=0))
        return PlayerWhite, PlayerBlack