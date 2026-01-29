import os
import time
#tahta ve sayılar
numbers = [1,2,3,4,5,6,7,8,9]

#dosya okuma ve tahtayı hazırlama
def prepare_board():
    with open("files/input.txt", "r", encoding="utf-8") as file:
        content = []
        for line in file:
            line = line.strip()
            if line:
                digits = [int(d) for d in line if d.isdigit()]
                if len(digits) > 0:
                    content.append(digits)
        return content

board = prepare_board()

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
def find_box_index(row,column):
    if column  > 9 or row > 9 or row <1 or column < 1:
        return False
    elif column  <= 3 and row <= 3:
        return 1
    elif (column  >=4 and column <=6) and (row <=3):
        return 2
    elif (column  >=7 and column  <=9) and (row <=3):
        return 3
    elif (column  >=1 and column  <=3) and (row >= 4 and row <= 6):
        return 4
    elif (column  >=4 and column  <=6) and (row >= 4 and row <= 6):
        return 5
    elif (column  >=7 and column  <=9) and (row >= 4 and row <= 6):
        return 6
    elif (column  >=1 and column  <=3) and (row >= 7 and row <= 9):
        return 7
    elif (column  >=4 and column  <=6) and (row >= 7 and row <= 9):
        return 8
    elif (column  >=7 and column  <=9) and (row >= 7 and row <= 9):
        return 9

#kontrol edici

def is_suitable(row,column,number):
    if number in rows(row):
        return False
    if number in columns(column):
        return False
    box_index = find_box_index(row,column)
    if number in boxs(box_index):
        return False
    return True
def explorer():
    for a in range(0, 9):
        for b in range(0, 9):
            if board[a][b] == 0:
                for c in range(1,10):
                    if is_suitable(a+1 , b+1 , c):
                        board[a][b] = c
                        if explorer():
                            return True
                        board[a][b] = 0
                return False
    return True
            
explorer()
print("Yazılıyor..")
time.sleep(2)
print("Tamamlandı , lütfen result.txt dosyasına bakınız , sonrasında kaydedip kapatmayı unutmayınız.")
time.sleep(3)
board_str = ""
for i in board:
    print(str(i))
    i = str(i)
    with open("files/result.txt","a",encoding="utf-8") as file:
        file.write(f"{i}\n")
with open("files/result.txt","a",encoding="utf-8") as file:
        file.write("\n---------------------------\n")
