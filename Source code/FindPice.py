def FindPice(ColumnInput, RowInput, PlayerTurn, Players):
    for i in range(8):
        for I in range(8):
            if PlayerTurn == "White":
                for obj in Players[0]:
                    count = Players[0].index(obj)
                    if ColumnInput == obj.CPos and RowInput == obj.RPos:
                        return obj.Type, obj.Player, obj.MoveCount, count, obj
            if PlayerTurn == "Black":
                for obj in Players[1]:
                    count = Players[1].index(obj)
                    if ColumnInput == obj.CPos and RowInput == obj.RPos:
                        # count is the pice in the players truple
                        return obj.Type, obj.Player, obj.MoveCount, count, obj
    return "There is no piece at chosen location"