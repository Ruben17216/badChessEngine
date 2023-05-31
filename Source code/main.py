from Veriables import *
from DrawBard import Board
from UserInputs import UserInput
from Check_CheckMate import CheckCheckmate, update_check
from Layout import layout

def main():
    Players = layout.default()
    PlayerWhite = Players[0];
    PlayerBlack = Players[1]
    PlayerTurn = 'White'
    print("Made by Ruben Hillier")
    print("Version: ", version)
    print('')

    while True:
        KingLowcationRowWhite, KingLowcationColumnWhite, KingLowcationRowBlack, KingLowcationColumnBlack = Board.draw(
            Players, Players)
        update_check(KingLowcationRowWhite, KingLowcationColumnWhite, KingLowcationRowBlack, KingLowcationColumnBlack,
                     PlayerWhite, PlayerBlack, Players, PlayerTurn)
        if I == True:
            print("It is", PlayerTurn, "turn")
            info = UserInput.PieceSelect(PlayerTurn, Players)
            PiceSelected = info[0];
            CPosMoveTo = info[1];
            RPosCurrent = info[2]
            PlayerTurn = UserInput.MovePiece(PiceSelected, PlayerTurn, RPosCurrent, CPosMoveTo, PlayerWhite,
                                             PlayerBlack, Players, KingLowcationRowWhite, KingLowcationColumnWhite, KingLowcationRowBlack, KingLowcationColumnBlack)


if __name__ == "__main__":
    main()

