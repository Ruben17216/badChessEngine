from Veriables import *
from FindPice import FindPice
from Pieces import *
class UserInput():
    def GetInputs(PlayerTurn, Players):
        while True:
            try:
                ColumnInput = input("Column: ")
                ColumnInput = Letters.index(ColumnInput)
                ColumnInput = ColumnInput + 1
                if ColumnInput > 8:
                    ColumnInput = ColumnInput - 8
                    break
                break
            except:
                print("You must not have enterd a Letter. Try again.")
        while True:
            try:
                RowInput = int(input("Row: "))
                if RowInput > 8:
                    print("Out of board")
                else:
                    RowInput = Numbers[RowInput]
                    break
            except:
                print("You must not have enterd a number. Try again.")

        return ColumnInput, RowInput

    def PieceSelect(PlayerTurn, Players):
        while True:
            ColumnInputRowInput = UserInput.GetInputs(PlayerTurn, Players)
            ColumnInput = ColumnInputRowInput[0]
            RowInput = ColumnInputRowInput[1]
            PiceSelected = FindPice(ColumnInput, RowInput, PlayerTurn, Players)
            PiceSelected = PiceSelected[0]
            if PiceSelected != "T":
                print("You have selected:", PiceSelected)
                break
            if PiceSelected == "T":
                print("There is no piece at chosen location")
        return PiceSelected, ColumnInput, RowInput

    def MovePiece(PiceSelected, PlayerTurn, RPosCurrent, CPosCurrent, PlayerWhite, PlayerBlack, Players, KingLowcationRowWhite, KingLowcationColumnWhite, KingLowcationRowBlack, KingLowcationColumnBlack):
        ColumnInputRowInput = UserInput.GetInputs(PlayerTurn, Players)
        ColumnInput = ColumnInputRowInput[0]
        RowInput = ColumnInputRowInput[1]
        if PiceSelected == "Pawn":
            info = Pawn.move(CPosCurrent, RPosCurrent, ColumnInput, RowInput, PlayerTurn, PlayerWhite, PlayerBlack, KingLowcationRowWhite, KingLowcationColumnWhite, KingLowcationRowBlack, KingLowcationColumnBlack, Players)
        if PiceSelected == "Knight":
            info = Knight.move(CPosCurrent, RPosCurrent, ColumnInput, RowInput, PlayerTurn, PlayerWhite, PlayerBlack, KingLowcationRowWhite, KingLowcationColumnWhite, KingLowcationRowBlack, KingLowcationColumnBlack, Players)
        if PiceSelected == "Bishop":
            info = Bishop.move(CPosCurrent, RPosCurrent, ColumnInput, RowInput, PlayerTurn, PlayerWhite, PlayerBlack, KingLowcationRowWhite, KingLowcationColumnWhite, KingLowcationRowBlack, KingLowcationColumnBlack, Players)
        if PiceSelected == "Rook":
            info = Rook.move(CPosCurrent, RPosCurrent, ColumnInput, RowInput, PlayerTurn, PlayerWhite, PlayerBlack, KingLowcationRowWhite, KingLowcationColumnWhite, KingLowcationRowBlack, KingLowcationColumnBlack, Players)
        if PiceSelected == "King":
            info = King.move(CPosCurrent, RPosCurrent, ColumnInput, RowInput, PlayerTurn, PlayerWhite, PlayerBlack, KingLowcationRowWhite, KingLowcationColumnWhite, KingLowcationRowBlack, KingLowcationColumnBlack, Players)
        if PiceSelected == "Queen":
            info = Queen.move(CPosCurrent, RPosCurrent, ColumnInput, RowInput, PlayerTurn, PlayerWhite, PlayerBlack, KingLowcationRowWhite, KingLowcationColumnWhite, KingLowcationRowBlack, KingLowcationColumnBlack, Players)
        if PlayerTurn == "Black" and info[0] == True:
            PlayerTurn = "White"
            return PlayerTurn
        if PlayerTurn == "White" and info[0] == True:
            PlayerTurn = "Black"
            return PlayerTurn
        return PlayerTurn