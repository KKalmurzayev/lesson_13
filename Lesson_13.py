
# print("*" * 10, "Задание №1 определение цвет клетки шахматной доски ", "*" * 10)
# try:
#     x1 = int(input("Введите столбец фигуры: ")) 
#     y1 = int(input("Введите строку фигуры: ")) 
#     x2 = int(input("Введите столбец фигуры: "))
#     y2 = int(input("Введите строку фигуры: ")) 
#     if (x1+y1) % 2 == (x2 + y2) % 2:
#         print("Yes")
        
#     else:
#         print("No")
# except ValueError:
#         print("Error, try again Input:")


# print("*" * 10, "Задание №1.1 ход ладьи в шахматной доске ", "*" * 10)
# try:
#     x1 = int(input("Введите столбец ладьи: "))
#     y1 = int(input("Введите строку ладьи: "))
#     x2 = int(input("Введите столбец фигуры: "))
#     y2 = int(input("Введите строку фигуры: "))    
#     if x1==x2 or y1 == y2:
#         print("Yes")
            
#     else:
#         print("No")
# except ValueError:
#         print("Error, try again Input:")


print("*" * 10, "Задание №2 ход кароля в шахматной доске ", "*" * 10)
try:
    x1 = int(input("Введите столбец короля: "))
    y1 = int(input("Введите строку корля: "))
    x2 = int(input("Введите столбец фигуры: "))
    y2 = int(input("Введите строку фигуры: "))    
    if max(abs(x1 - x2), abs(y1-y2))==1:
        print("Yes")
            
    else:
        print("No")
except ValueError:
        print("Error, try again Input:")





