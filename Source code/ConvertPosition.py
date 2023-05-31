import math

class ConvertPosition:
    def GetColumnAndRow(Position):
        row_num = math.ceil(Position / 8)
        column_num = abs(((row_num * 8) - Position) - 8)
        return column_num, row_num

    def GetPoition(col, row):
        position = (row - 1) * 8 + col
        return position