from ConvertPosition import ConvertPosition
from FindPice import FindPice
from Check_CheckMate import *

def MovingLogic(CPosCurrent, RPosCurrent, CPosMoveTo, RPosMoveTo, PlayerTurn, PlayerWhite, PlayerBlack, DistanceToCheck, CheckDepth, KingLowcationRowWhite, KingLowcationColumnWhite, KingLowcationRowBlack, KingLowcationColumnBlack, Players):
    list = ["Black", "White"]
    Position = ConvertPosition.GetPoition(CPosCurrent, RPosCurrent)
    if PlayerTurn == "White":
        KingLowcationRow = KingLowcationRowWhite
        KingLowcationColumn = KingLowcationColumnWhite
    if PlayerTurn == "Black":
        KingLowcationRow = KingLowcationRowBlack
        KingLowcationColumn = KingLowcationColumnBlack

    for l, item in enumerate(list):
        if l == 1:
            l = -1
        if PlayerTurn == item:
            info = FindPice(CPosCurrent, RPosCurrent, item, Players)
            obj = info[4]
            for i in range(CheckDepth):
                PossibleMove = Position + (DistanceToCheck * i)
                CRPos = ConvertPosition.GetColumnAndRow(PossibleMove)
                CPos = CRPos[0]
                RPos = CRPos[1]
                info = FindPice(CPos, RPos, item, Players)
                if info == "There is no piece at chosen location" or (CPos == CPosCurrent and RPos == RPosCurrent):
                    info = FindPice(CPos, RPos, list[l + 1], Players)
                    if info == "There is no piece at chosen location":
                        if CPosMoveTo == CPos and RPosMoveTo == RPos:
                            CPosBackup = obj.CPos; obj.CPos = CPosMoveTo
                            RposBackup = obj.RPos; obj.RPos = RPosMoveTo
                            obj.MoveCount = obj.MoveCount + 1
                            check = CheckCheckmate.check_for_check(KingLowcationRow, KingLowcationColumn, PlayerWhite, PlayerBlack, PlayerTurn, Players)
                            if check[0] == True:
                                print("invalied Move you are in check")
                                obj.CPos = CPosBackup
                                obj.RPos = RposBackup
                                obj.MoveCount = obj.MoveCount - 1
                                return False, ("invalied Move you are in check")
                            return True, " "
                    else:
                        if CPosMoveTo == CPos and RPosMoveTo == RPos:
                            info = FindPice(CPosMoveTo, RPosMoveTo, list[l + 1], Players)
                            count = info[3]; type = info[0]
                            if item == "White":
                                del PlayerBlack[count]
                            if item == "Black":
                                del PlayerWhite[count]
                            CPosBackup = obj.CPos;
                            obj.CPos = CPosMoveTo
                            RposBackup = obj.RPos;
                            obj.RPos = RPosMoveTo
                            obj.MoveCount = obj.MoveCount + 1
                            check = CheckCheckmate.check_for_check(KingLowcationRow, KingLowcationColumn, PlayerWhite, PlayerBlack, PlayerTurn, Players)
                            if check[0] == True:
                                print("invalied Move you are in check")
                                obj.CPos = CPosBackup
                                obj.RPos = RposBackup
                                obj.MoveCount = obj.MoveCount - 1
                                if item == "White":
                                    PlayerBlack.append(
                                        Rook(Type=info[0], Player="Black", CPos=CPosMoveTo, RPos=RPosMoveTo, MoveCount=info[2]))
                                if item == "Black":
                                    PlayerWhite.append(
                                        Rook(Type=info[0], Player="White", CPos=CPosMoveTo, RPos=RPosMoveTo, MoveCount=info[2]))
                                return False, ("invalied Move you are in check")
                            return True, type
                        else:
                            return False, ("invalid Move. Cant move over a pice!")
                else:
                    return False, ("invalid Move. Cant move over or to one of your own pice!")