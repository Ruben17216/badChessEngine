from MoveLogic import MovingLogic
from ConvertPosition import ConvertPosition
from FindPice import FindPice
from Check_CheckMate import *

class Piece(object):
    def __init__(self, Type, Player, CPos, RPos, MoveCount):
        self.Type = Type
        self.Player = Player
        self.CPos = CPos
        self.RPos = RPos
        self.MoveCount = MoveCount

class Pawn(Piece):
    def move(CPosCurrent, RPosCurrent, CPosMoveTo, RPosMoveTo, PlayerTurn, PlayerWhite, PlayerBlack, KingLowcationRowWhite, KingLowcationColumnWhite, KingLowcationRowBlack, KingLowcationColumnBlack, Players):
        if PlayerTurn == "White":
            KingLowcationRow = KingLowcationRowWhite
            KingLowcationColumn = KingLowcationColumnWhite
        if PlayerTurn == "Black":
            KingLowcationRow = KingLowcationRowBlack
            KingLowcationColumn = KingLowcationColumnBlack
        list = ["Black", "White"]
        NumberOfRowMoved = RPosMoveTo - RPosCurrent; NumberOfColumnMoved = abs(CPosMoveTo - CPosCurrent)
        for i, item in enumerate(list):
            offset = 0
            if i == 1:
                i = -1
                offset = -2
            if PlayerTurn == item:
                MoveCount = FindPice(CPosCurrent, RPosCurrent, item, Players)
                obj = MoveCount[4]
                MoveCount = MoveCount[2]
                if int(MoveCount) == 0:
                    info = FindPice(CPosMoveTo, RPosMoveTo, item, Players)
                    if abs(NumberOfRowMoved) == 2:
                        info2 = FindPice(CPosMoveTo, RPosMoveTo - 1-(offset*1), item, Players)
                        info3 = FindPice(CPosMoveTo, RPosMoveTo - 1 - (offset * 1), list[i + 1], Players)
                    else:
                        info2 = "There is no piece at chosen location"
                        info3 = "There is no piece at chosen location"
                    if info == "There is no piece at chosen location" and info2 == "There is no piece at chosen location" and info3 == "There is no piece at chosen location":
                        if abs(NumberOfRowMoved) <= 2:
                            info = FindPice(CPosMoveTo, RPosMoveTo, list[i+1], Players)
                            #print(list[i + 1], info[0], PlayerBlack[info[3]], PlayerWhite[info[3]], 1+(offset*1), NumberOfColumnMoved)
                            count = info[3]
                            if info != "There is no piece at chosen location" and NumberOfColumnMoved == 1+(offset*1):
                                if item == "White":
                                    del PlayerBlack[count]
                                if item == "Black":
                                    del PlayerWhite[count]
                                print("hihig")
                                CPosBackup = obj.CPos; RposBackup = obj.RPos
                                obj.CPos = CPosMoveTo; obj.RPos = RPosMoveTo; obj.MoveCount = obj.MoveCount + 1
                                check = CheckCheckmate.check_for_check(KingLowcationRow, KingLowcationColumn,
                                                                       PlayerWhite, PlayerBlack, PlayerTurn, Players)
                                if check[0] == True:
                                    print("invalied Move you are in check")
                                    obj.CPos = CPosBackup
                                    obj.RPos = RposBackup
                                    obj.MoveCount = obj.MoveCount - 1
                                    if item == "White":
                                        PlayerBlack.append(
                                            Rook(Type=info[0], Player="Black", CPos=CPosMoveTo, RPos=RPosMoveTo,
                                                 MoveCount=info[2]))
                                    if item == "Black":
                                        PlayerWhite.append(
                                            Rook(Type=info[0], Player="White", CPos=CPosMoveTo, RPos=RPosMoveTo,
                                                 MoveCount=info[2]))
                                    return False, ("invalied Move you are in check")
                                return True, info[0]
                            if info == "There is no piece at chosen location" and NumberOfColumnMoved == 0:
                                CPosBackup = obj.CPos; RposBackup = obj.RPos
                                obj.CPos = CPosMoveTo; obj.RPos = RPosMoveTo; obj.MoveCount = obj.MoveCount + 1
                                check = CheckCheckmate.check_for_check(KingLowcationRow, KingLowcationColumn, PlayerWhite, PlayerBlack, PlayerTurn, Players)
                                if check[0] == True:
                                    print("invalied Move you are in check")
                                    obj.CPos = CPosBackup
                                    obj.RPos = RposBackup
                                    obj.MoveCount = obj.MoveCount - 1
                                    return False, ("invalied Move you are in check")
                                if abs(NumberOfRowMoved) == 2:
                                    if item == "White":
                                        PlayerWhite.append(
                                            PasontDot(Type=".PasontDot", Player="White", CPos=CPosMoveTo,
                                                      RPos=RPosMoveTo + 1,
                                                      MoveCount=0))
                                    if item == "Black":
                                        PlayerBlack.append(
                                            PasontDot(Type=".PasontDot", Player="Black", CPos=CPosMoveTo,
                                                      RPos=RPosMoveTo - 1,
                                                      MoveCount=0))
                                return True, " "
                            else:
                                return False, ("invalid Move. You are moving to far!")
                        else:
                            return False, ("invalid Move. You are moving to far!")
                    else:
                        return False, ("invalid Move. Cant move to were another of your pieces are!")
                if int(MoveCount) > 0:
                    info = FindPice(CPosMoveTo, RPosMoveTo, item, Players)
                    if info == "There is no piece at chosen location":
                        print(1+(offset+2), offset)
                        if NumberOfRowMoved == 1+(offset):
                            info = FindPice(CPosMoveTo, RPosMoveTo, list[i + 1], Players)
                            print(list[i + 1])
                            count = info[3]
                            if info != "There is no piece at chosen location" and NumberOfColumnMoved == 1+(offset*1):
                                if info[0] == ".PasontDot":
                                    if item == "White":
                                        info = FindPice(CPosMoveTo, RPosMoveTo+1, "Black", Players)
                                    if item == "Black":
                                        info = FindPice(CPosMoveTo, RPosMoveTo-1, "White", Players)
                                    count = info[3]
                                if item == "White":
                                    del PlayerBlack[count]
                                if item == "Black":
                                    del PlayerWhite[count]
                                CPosBackup = obj.CPos; RposBackup = obj.RPos
                                obj.CPos = CPosMoveTo; obj.RPos = RPosMoveTo; obj.MoveCount = obj.MoveCount + 1
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
                                return True, info[0]
                            if info == "There is no piece at chosen location" and NumberOfColumnMoved == 0:
                                CPosBackup = obj.CPos; RposBackup = obj.RPos
                                obj.CPos = CPosMoveTo; obj.RPos = RPosMoveTo; obj.MoveCount = obj.MoveCount + 1
                                check = CheckCheckmate.check_for_check(KingLowcationRow, KingLowcationColumn, PlayerWhite, PlayerBlack, PlayerTurn, Players)
                                if check[0] == True:
                                    print("invalied Move you are in check")
                                    obj.CPos = CPosBackup
                                    obj.RPos = RposBackup
                                    obj.MoveCount = obj.MoveCount - 1
                                    return False, ("invalied Move you are in check")
                            else:
                                return False, ("invalid Move. You are moving to far!")
                        else:
                            return False, ("invalid Move. You are moving to far!")
                    else:
                        return False, ("invalid Move. Cant move to were another of your pieces are!")

class Queen(Piece):
    def move(CPosCurrent, RPosCurrent, CPosMoveTo, RPosMoveTo, PlayerTurn, PlayerWhite, PlayerBlack, KingLowcationRowWhite, KingLowcationColumnWhite, KingLowcationRowBlack, KingLowcationColumnBlack, Players):
        list = ["White", "Black"]
        # finding in which direction the piece is moving
        if RPosCurrent > RPosMoveTo and CPosCurrent == CPosMoveTo:
            DistanceToCheck = -8
        elif RPosCurrent < RPosMoveTo and CPosCurrent == CPosMoveTo:
            DistanceToCheck = 8
        elif RPosCurrent == RPosMoveTo and CPosCurrent > CPosMoveTo:
            DistanceToCheck = -1
        elif RPosCurrent == RPosMoveTo and CPosCurrent < CPosMoveTo:
            DistanceToCheck = 1
        elif RPosCurrent > RPosMoveTo and CPosCurrent < CPosMoveTo:
            DistanceToCheck = -7
        elif RPosCurrent > RPosMoveTo and CPosCurrent > CPosMoveTo:
            DistanceToCheck = -9
        elif RPosCurrent < RPosMoveTo and CPosCurrent < CPosMoveTo:
            DistanceToCheck = 9
        elif RPosCurrent < RPosMoveTo and CPosCurrent > CPosMoveTo:
            DistanceToCheck = 7
        else:
            return False, "invalid Move."

        info = MovingLogic(CPosCurrent, RPosCurrent, CPosMoveTo, RPosMoveTo, PlayerTurn, PlayerWhite, PlayerBlack, DistanceToCheck, 8, KingLowcationRowWhite, KingLowcationColumnWhite, KingLowcationRowBlack, KingLowcationColumnBlack, Players)
        return info

class King(Piece):
    def move(CPosCurrent, RPosCurrent, CPosMoveTo, RPosMoveTo, PlayerTurn, PlayerWhite, PlayerBlack, KingLowcationRowWhite, KingLowcationColumnWhite, KingLowcationRowBlack, KingLowcationColumnBlack, Players):
        if PlayerTurn == "White":
            KingLowcationRow = KingLowcationRowWhite
            KingLowcationColumn = KingLowcationColumnWhite
        if PlayerTurn == "Black":
            KingLowcationRow = KingLowcationRowBlack
            KingLowcationColumn = KingLowcationColumnBlack
        list = ["White", "Black"]
        # finding in which direction the piece is moving
        if RPosCurrent > RPosMoveTo and CPosCurrent == CPosMoveTo:
            DistanceToCheck = -8
        elif RPosCurrent < RPosMoveTo and CPosCurrent == CPosMoveTo:
            DistanceToCheck = 8
        elif RPosCurrent == RPosMoveTo and CPosCurrent > CPosMoveTo:
            DistanceToCheck = -1
        elif RPosCurrent == RPosMoveTo and CPosCurrent < CPosMoveTo:
            DistanceToCheck = 1
        elif RPosCurrent > RPosMoveTo and CPosCurrent < CPosMoveTo:
            DistanceToCheck = -7
        elif RPosCurrent > RPosMoveTo and CPosCurrent > CPosMoveTo:
            DistanceToCheck = -9
        elif RPosCurrent < RPosMoveTo and CPosCurrent < CPosMoveTo:
            DistanceToCheck = 9
        elif RPosCurrent < RPosMoveTo and CPosCurrent > CPosMoveTo:
            DistanceToCheck = 7
        else:
            return False, 'invalid Move.'
        info = FindPice(CPosCurrent, RPosCurrent, PlayerTurn, Players)
        MoveCount = info[2]
        if PlayerTurn == "Black":
            a = 1; b = 0; c = 0; d = 0
        if PlayerTurn == "White":
            a = 8; b = 7
        if (MoveCount == 0 and CPosMoveTo == 1 and RPosMoveTo == a) or (MoveCount == 0 and CPosMoveTo == 8 and RPosMoveTo == a):
            if CPosMoveTo == 1 and RPosMoveTo == a:
                for i in range(3):
                    Pice = FindPice(i+2, 1+b, PlayerTurn, Players)
                    if Pice == "There is no piece at chosen location":
                        info = FindPice(1, a, PlayerTurn, Players)
                        MoveCount = info[2]
                        Piece = info[0]
                        if MoveCount == 0 and Piece == "Rook":
                            obj = info[4]
                            CPosBackup = obj.CPos; obj.CPos = 4
                            RposBackup = obj.RPos; obj.RPos = 1+b
                            obj.MoveCount = obj.MoveCount + 1
                            check = CheckCheckmate.check_for_check(KingLowcationRow, KingLowcationColumn, PlayerWhite,
                                                                   PlayerBlack, PlayerTurn, Players)
                            if check[0] == True:
                                print("invalied Move you are in check")
                                obj.CPos = CPosBackup
                                obj.RPos = RposBackup
                                obj.MoveCount = obj.MoveCount - 1
                                return False, ("invalied Move you are in check")
                            info = FindPice(CPosCurrent, RPosCurrent, PlayerTurn, Players)
                            obj = info[4]
                            CPosBackup = obj.CPos; obj.CPos = 3
                            RposBackup = obj.RPos; obj.RPos = 1+b
                            obj.MoveCount = obj.MoveCount + 1
                            check = CheckCheckmate.check_for_check(KingLowcationRow, KingLowcationColumn, PlayerWhite, PlayerBlack, PlayerTurn, Players)
                            if check[0] == True:
                                print("invalied Move you are in check")
                                obj.CPos = CPosBackup
                                obj.RPos = RposBackup
                                obj.MoveCount = obj.MoveCount - 1
                                return False, ("invalied Move you are in check")
                            return True, " "
            if CPosMoveTo == 8 and RPosMoveTo == a:
                for i in range(2):
                    Pice = FindPice(i + 6, 1 + b, PlayerTurn, Players)
                    if Pice == "There is no piece at chosen location":
                        info = FindPice(8, a, PlayerTurn, Players)
                        MoveCount = info[2]
                        obj = info[4]
                        Piece = obj.Type
                        if MoveCount == 0 and Piece == "Rook":
                            obj = info[4]
                            CPosBackup = obj.CPos; obj.CPos = 6
                            RposBackup = obj.RPos; obj.RPos = 1 + b
                            obj.MoveCount = obj.MoveCount + 1
                            check = CheckCheckmate.check_for_check(KingLowcationRow, KingLowcationColumn, PlayerWhite, PlayerBlack, PlayerTurn, Players)
                            if check[0] == True:
                                print("invalied Move you are in check")
                                obj.CPos = CPosBackup
                                obj.RPos = RposBackup
                                obj.MoveCount = obj.MoveCount - 1
                                return False, ("invalied Move you are in check")
                            info = FindPice(CPosCurrent, RPosCurrent, PlayerTurn, Players)
                            obj = info[4]
                            CPosBackup = obj.CPos; obj.CPos = 7
                            RposBackup = obj.RPos; obj.RPos = 1 + b
                            obj.MoveCount = obj.MoveCount + 1
                            check = CheckCheckmate.check_for_check(KingLowcationRow, KingLowcationColumn, PlayerWhite, PlayerBlack, PlayerTurn, Players)
                            if check[0] == True:
                                print("invalied Move you are in check")
                                obj.CPos = CPosBackup
                                obj.RPos = RposBackup
                                obj.MoveCount = obj.MoveCount - 1
                                return False, ("invalied Move you are in check")
                            return True, " "
        info = MovingLogic(CPosCurrent, RPosCurrent, CPosMoveTo, RPosMoveTo, PlayerTurn, PlayerWhite, PlayerBlack, DistanceToCheck, 2, KingLowcationRowWhite, KingLowcationColumnWhite, KingLowcationRowBlack, KingLowcationColumnBlack, Players)
        return info

class Bishop(Piece):
    def move(CPosCurrent, RPosCurrent, CPosMoveTo, RPosMoveTo, PlayerTurn, PlayerWhite, PlayerBlack, KingLowcationRowWhite, KingLowcationColumnWhite, KingLowcationRowBlack, KingLowcationColumnBlack, Players):
        # finding in which direction the piece is moving
        if RPosCurrent > RPosMoveTo and CPosCurrent < CPosMoveTo:
            DistanceToCheck = -7
        elif RPosCurrent > RPosMoveTo and CPosCurrent > CPosMoveTo:
            DistanceToCheck = -9
        elif RPosCurrent < RPosMoveTo and CPosCurrent < CPosMoveTo:
            DistanceToCheck = 9
        elif RPosCurrent < RPosMoveTo and CPosCurrent > CPosMoveTo:
            DistanceToCheck = 7
        else:
            return False, ("invalid Move.")

        info = MovingLogic(CPosCurrent, RPosCurrent, CPosMoveTo, RPosMoveTo, PlayerTurn, PlayerWhite, PlayerBlack, DistanceToCheck, 8, KingLowcationRowWhite, KingLowcationColumnWhite, KingLowcationRowBlack, KingLowcationColumnBlack, Players)
        return info

class Knight(Piece):
    def move(CPosCurrent, RPosCurrent, CPosMoveTo, RPosMoveTo, PlayerTurn, PlayerWhite, PlayerBlack, KingLowcationRowWhite, KingLowcationColumnWhite, KingLowcationRowBlack, KingLowcationColumnBlack, Players):
        if PlayerTurn == "White":
            KingLowcationRow = KingLowcationRowWhite
            KingLowcationColumn = KingLowcationColumnWhite
        if PlayerTurn == "Black":
            KingLowcationRow = KingLowcationRowBlack
            KingLowcationColumn = KingLowcationColumnBlack
        if RPosCurrent < RPosMoveTo and CPosCurrent < CPosMoveTo:
            DistanceToCheck1 = 10
            DistanceToCheck2 = 17
        elif RPosCurrent < RPosMoveTo and CPosCurrent > CPosMoveTo:
            DistanceToCheck1 = 6
            DistanceToCheck2 = 15
        elif RPosCurrent > RPosMoveTo and CPosCurrent > CPosMoveTo:
            DistanceToCheck1 = -10
            DistanceToCheck2 = -17
        elif RPosCurrent > RPosMoveTo and CPosCurrent < CPosMoveTo:
            DistanceToCheck1 = -6
            DistanceToCheck2 = -15
        else:
            return False, ("invalid Move. The Knight can only move in L shape")
        list = ["Black", "White"]
        Position = ConvertPosition.GetPoition(CPosCurrent, RPosCurrent)
        for l, item in enumerate(list):
            if l == 1:
                l = -1
            if PlayerTurn == item:
                info = FindPice(CPosCurrent, RPosCurrent, item, Players)
                obj = info[4]
                for i in range(2):
                    PossibleMove1 = Position + (DistanceToCheck1 * i)
                    PossibleMove2 = Position + (DistanceToCheck2 * i)
                    CRPos1 = ConvertPosition.GetColumnAndRow(PossibleMove1)
                    CPos1 = CRPos1[0]; RPos1 = CRPos1[1]
                    CRPos2 = ConvertPosition.GetColumnAndRow(PossibleMove2)
                    CPos2 = CRPos2[0]; RPos2 = CRPos2[1]
                    if CPos1 == CPosMoveTo and RPos1 == RPosMoveTo:
                        info = FindPice(CPos1, RPos1, item, Players)
                    if CPos2 == CPosMoveTo and RPos2 == RPosMoveTo:
                        info = FindPice(CPos2, RPos2, item, Players)
                    if (info == "There is no piece at chosen location") or (CPos1 == CPosCurrent and RPos1 == RPosCurrent) or (CPos2 == CPosCurrent and RPos2 == RPosCurrent):
                        Continue = False
                        if CPos1 == CPosMoveTo and RPos1 == RPosMoveTo:
                            info = FindPice(CPos1, RPos1, list[l + 1], Players)
                            Continue = True
                        elif CPos2 == CPosMoveTo and RPos2 == RPosMoveTo:
                            info = FindPice(CPos2, RPos2, list[l + 1], Players)
                            Continue = True
                        else:
                            Continue = "Self"
                        if info == "There is no piece at chosen location" and Continue == True:
                            if CPosMoveTo == CPos1 or CPos2 and RPosMoveTo == RPos1 or RPos2:
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
                            if CPosMoveTo == CPos1 or CPos2 and RPosMoveTo == RPos1 or RPos2:
                                if Continue != "Self":
                                    info = FindPice(CPosMoveTo, RPosMoveTo, list[l + 1], Players)
                                    count = info[3]; type = info[0]
                                    if item == "White":
                                        del PlayerBlack[count]
                                    if item == "Black":
                                        del PlayerWhite[count]
                                    CPosBackup = obj.CPos; obj.CPos = CPosMoveTo
                                    RposBackup = obj.RPos; obj.RPos = RPosMoveTo
                                    obj.MoveCount = obj.MoveCount + 1
                                    check = CheckCheckmate.check_for_check(KingLowcationRow, KingLowcationColumn, PlayerWhite, PlayerBlack, PlayerTurn, Players)
                                    if check[0] == True:
                                        print("invalied Move you are in check")
                                        obj.CPos = CPosBackup
                                        obj.RPos = RposBackup
                                        obj.MoveCount = obj.MoveCount - 1
                                        if item == "White":
                                            PlayerBlack.append(
                                                Rook(Type=info[0], Player="Black", CPos=CPosMoveTo, RPos=RPosMoveTo,
                                                     MoveCount=info[2]))
                                        if item == "Black":
                                            PlayerWhite.append(
                                                Rook(Type=info[0], Player="White", CPos=CPosMoveTo, RPos=RPosMoveTo,
                                                     MoveCount=info[2]))
                                        return False, ("invalied Move you are in check")
                                    return True, type
                            else:
                                return False, ("invalid Move. Cant move over a pice!")
                    else:
                        return False, ("invalid Move. Cant move over or to one of your own pice!")

class Rook(Piece):
    def move(CPosCurrent, RPosCurrent, CPosMoveTo, RPosMoveTo, PlayerTurn, PlayerWhite, PlayerBlack, KingLowcationRowWhite, KingLowcationColumnWhite, KingLowcationRowBlack, KingLowcationColumnBlack, Players):
        # finding in which direction the piece is moving
        if RPosCurrent > RPosMoveTo and CPosCurrent == CPosMoveTo:
            Direction = "Up"
            DistanceToCheck = -8
        elif RPosCurrent < RPosMoveTo and CPosCurrent == CPosMoveTo:
            Direction = "Down"
            DistanceToCheck = 8
        elif RPosCurrent == RPosMoveTo and CPosCurrent > CPosMoveTo:
            Direction = "Left"
            DistanceToCheck = -1
        elif RPosCurrent == RPosMoveTo and CPosCurrent < CPosMoveTo:
            Direction = "Right"
            DistanceToCheck = 1
        else:
            return False, "invalid Move. The rook can only move horizontal or vertical"

        info = MovingLogic(CPosCurrent, RPosCurrent, CPosMoveTo, RPosMoveTo, PlayerTurn, PlayerWhite, PlayerBlack, DistanceToCheck, 8, KingLowcationRowWhite, KingLowcationColumnWhite, KingLowcationRowBlack, KingLowcationColumnBlack, Players)
        return info

class PasontDot(Piece):
    pass