from ConvertPosition import ConvertPosition
from FindPice import FindPice

class CheckCheckmate:
    def check_for_check(KingLowcationRow, KingLowcationColumn, PlayerWhite, PlayerBlack, PlayerTurn, Players, King=False):
        KingPos = ConvertPosition.GetPoition(KingLowcationColumn, KingLowcationRow)
        MoveCheckDirections = [8, -8, -1, 1, -7, -9, 9, 7, 10, -10, 17, -17, 6, -6, 15, -15, 7, 9, -7, -9]
        for list_pos, CheckDirections in enumerate(MoveCheckDirections):
            CheckSquare = KingPos
            for i in range(8):
                CheckSquare = CheckSquare + CheckDirections
                c, r = ConvertPosition.GetColumnAndRow(CheckSquare)

                #making sure that check deepth is not going to far
                if (list_pos == 2 or list_pos == 3) and r > KingLowcationRow:
                    break
                if (list_pos == 2 or list_pos == 3) and r < KingLowcationRow:
                    break
                if (list_pos == 0 or list_pos == 1) and c > KingLowcationColumn:
                    break
                if (list_pos == 0 or list_pos == 1) and c < KingLowcationColumn:
                    break
                if c > 9 or r > 9 or c < 1 or r < 1:
                    break

                if PlayerTurn == "Black":
                    info = FindPice(c, r, PlayerTurn, Players)
                    if info[0] != "T":
                        if info[0] != "King" and King == True:
                            break
                        if info[0] != "T" and King == False:
                            break
                    if info[0] == "King" and King == True:
                        info = ["T", info[2], info[3], info[4]]
                    else:
                        info = FindPice(c, r, "White", Players)
                if PlayerTurn == "White":
                    info = FindPice(c, r, PlayerTurn, Players)
                    if info[0] != "T":
                        if info[0] != "King" and King == True:
                            break
                        if info[0] != "T" and King == False:
                            break
                    if info[0] == "King" and King == True:
                        info = ["T", info[2], info[3], info[4]]
                    else:
                        info = FindPice(c, r, "Black", Players)
                if (info[0] == "Rook" or  info[0] == "Queen") and (list_pos <= 3):
                    return True, list_pos, "Straight"
                if (info[0] == "Bishop" or  info[0] == "Queen") and (list_pos > 3 and list_pos <= 7):
                    return True, list_pos, "Diagonal"
                if info[0] == "King" and i == 0 and list_pos <= 7:
                    return True, list_pos, "King"
                if info[0] == "Knight" and list_pos > 7 and i == 0 and list_pos <= 15:
                    return True, list_pos, "Knight"
                if info[0] == "Pawn" and list_pos > 17 and i == 0 and PlayerTurn == "White":
                    return True, list_pos, "PawnBlack"
                if info[0] == "Pawn" and list_pos > 15 and list_pos <= 17 and i == 0 and PlayerTurn == "Black":
                    return True, list_pos, "PawnWhite"
                if info[0] != "T":
                    break
        return False, 0, 0

    def check_for_mate(KingLowcationRow, KingLowcationColumn, PlayerWhite, PlayerBlack, PlayerTurn, Players):
        MoveCheckDirections = [1, 9, 8, 7, -1, -9, -8, -7]
        MoveCheckDirections2 = [8, -8, -1, 1, -7, -9, 9, 7, 10, -10, 17, -17, 6, -6, 15, -15, 7, 9, -7, -9]
        KingPos = ConvertPosition.GetPoition(KingLowcationColumn, KingLowcationRow)
        for i, I in enumerate(MoveCheckDirections):
            KingPos = ConvertPosition.GetPoition(KingLowcationColumn, KingLowcationRow)
            KingPos = KingPos + I
            c, r =ConvertPosition.GetColumnAndRow(KingPos)
            check = CheckCheckmate.check_for_check(r, c, PlayerWhite, PlayerBlack, PlayerTurn, Players, King=True)
            if c > 8 or c < 1 or r > 8 or r < 1:
                check[0] = True
            info = "T"; info2 = "T"
            if PlayerTurn == "White":
                info = FindPice(c, r, "White", Players)
            if PlayerTurn == "Black":
                info2 = FindPice(c, r, "Black", Players)
            if info[0] == "There is no piece at chosen location" or info2[0] == "There is no piece at chosen location" or info[0] == "T" or info2[0] == "T":
                if check[0] == False:
                    return False
        KingPos = ConvertPosition.GetPoition(KingLowcationColumn, KingLowcationRow)
        check = CheckCheckmate.check_for_check(KingLowcationRow, KingLowcationColumn, PlayerWhite, PlayerBlack, PlayerTurn, Players)
        CheckDirection = MoveCheckDirections2[check[1]]
        CheckDepth = 8
        if check[2] != "Knight":
            KingPos = KingPos + CheckDirection
            CheckDepth = 1
        for i in range(CheckDepth):
            KingPos = ConvertPosition.GetPoition(KingLowcationColumn, KingLowcationRow)
            KingPos = KingPos + CheckDirection
            c, r = ConvertPosition.GetColumnAndRow(KingPos)
            if PlayerTurn == "White":
                check = CheckCheckmate.check_for_check(r, c, PlayerWhite, PlayerBlack, "White", Players)
            if PlayerTurn == "Black":
                check = CheckCheckmate.check_for_check(r, c, PlayerWhite, PlayerBlack, "Black", Players)
            if check[0] == False:
                return False
        #not yet finished
        return True

def update_check(KingLowcationRowWhite, KingLowcationColumnWhite, KingLowcationRowBlack, KingLowcationColumnBlack, PlayerWhite, PlayerBlack, Players, PlayerTurn):
    for i in range(2):
        if i == 0:
            KingLowcationRow = KingLowcationRowWhite
            KingLowcationColumn = KingLowcationColumnWhite
            PlayerTurnInfo = "White"
            IsCheck = CheckCheckmate.check_for_check(KingLowcationRow, KingLowcationColumn, PlayerWhite, PlayerBlack, PlayerTurnInfo, Players)
            if IsCheck[0] == True:
                print("White is in Check")
                PlayerTurn == "White"
                WhiteCheck = True
                IsCheckMate = CheckCheckmate.check_for_mate(KingLowcationRow, KingLowcationColumn, PlayerWhite,PlayerBlack, PlayerTurnInfo)
                if IsCheckMate == True:
                    #while True:
                    print("Black Wins by check mate")
        if i == 1:
            KingLowcationRow = KingLowcationRowBlack
            KingLowcationColumn = KingLowcationColumnBlack
            PlayerTurnInfo = "Black"
            IsCheck = CheckCheckmate.check_for_check(KingLowcationRow, KingLowcationColumn, PlayerWhite, PlayerBlack, PlayerTurnInfo, Players)
            if IsCheck[0] == True:
                print("Black is in Check")
                PlayerTurn == "Black"
                BlackCheck = True
                IsCheckMate = CheckCheckmate.check_for_mate(KingLowcationRow, KingLowcationColumn, PlayerWhite, PlayerBlack, PlayerTurnInfo, Players)
                if IsCheckMate == True:
                    print("White Wins by check mate")
                    i = True
                    while i:
                        response = input("Close window type Y: ")
                        if response == "Y":
                            i = False
                            I = False