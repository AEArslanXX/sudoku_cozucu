#tahta ve sayılar

numbers = [1,2,3,4,5,6,7,8,9]
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

#satır , sütun ve boxlara ayırma

columns_list = []
boxs_list = []
def columns(n):
    if n > 9:
        return False
    n -= 1
    collumns_data = []
    for row in range(9):
            collumns_data.append(board[row][n])
    return collumns_data
def rows(n):
    if n > 9:
        return False
    n -= 1
    return board[n]
def boxs(n):

    a = 0
    row_num = range(0)
    if n > 9:
        return False
    elif n == 1:
        a, row_num = 0, range(1,4)
    elif n == 2:
        a, row_num = 3, range(1,4)
    elif n == 3:
        a, row_num = 6, range(1,4)
    elif n == 4:
        a, row_num = 0, range(4,7)
    elif n == 5:
        a, row_num = 3, range(4,7)
    elif n == 6:
        a, row_num = 6, range(4,7)
    elif n == 7:
        a, row_num = 0, range(7,10)
    elif n == 8:
        a, row_num = 3, range(7,10)
    elif n == 9:
        a, row_num = 6, range(7,10)
    
    box_data = []
    for i in row_num:
        box_data.extend(rows(i)[a:a+3])
    return box_data
for i in range(1,10):
    columns_list.append(columns(i))
for i in range(1,10):
    boxs_list.append(boxs(i))

#kayıp sayıları bulma fonksiyonları

def find_number_rows():
        numbers_in = [] 
        for a in range(0, 9): 
            rows_in = [] 
            for b in range(0, 9): 
                num = board[a][b]
                if num != 0: 
                    rows_in.append(num) 
            numbers_in.append(rows_in) 
        
        missing_nums = []
        for i in range(len(numbers_in)):
            diffrence = list(set(numbers) - set(numbers_in[i]))
            missing_nums.append(diffrence)
        
        return missing_nums
def find_number_columns():
    numbers_in = []
    for a in range(0,9):
        columns_in = []
        for b in range(0,9):
            num = columns_list[a][b]
            if num != 0:
                columns_in.append(num)
        numbers_in.append(columns_in)
    missing_nums = []
    for i in range(len(numbers_in)):
            difference = list(set(numbers) - set(numbers_in[i]))
            missing_nums.append(difference)
    return missing_nums
def find_number_boxs():
    numbers_in = []
    for a in range(0,9):
        boxs_in = []
        for b in range(0,9):
            num = boxs_list[a][b]
            if num != 0:
                boxs_in.append(num)
        numbers_in.append(boxs_in)
    missing_nums = []
    for i in range(len(numbers_in)):
            difference = list(set(numbers) - set(numbers_in[i]))
            missing_nums.append(difference)
    return missing_nums

#kontrol edici

