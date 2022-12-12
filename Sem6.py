# Sem6
import random

# Показать разделитель
def printLiner():
    print("_ " * 20)
# Показать карту
# что бы вывести карту противника
# showMap(mapComputer)
def showMap(mapItem):
    printLiner()
    # показать колонки
    for row in range(len(mapItem[0])):
        print(row, end=" ")
    print()
    print("_ " * len(mapItem[0]))

    for column in range(len(mapItem)):
        for row in range(len(mapItem[column])):
            print(mapItem[column][row], end=" ")
        # показать строки
        print(" | ", column)
    printLiner()

# Создаем корабли
def generateComputerMap(mapItem, matrix, count = 1):
    comp_ship_points = count
    comp_filled_points = []

    while len(comp_filled_points) < comp_ship_points:
        column = random.randint(0, matrix - 1)
        row = random.randint(0, matrix - 1)

        isExist = False
        for v in comp_filled_points:
            if str(v) == str((column, row)):
                isExist = True
                break

        if isExist:
            continue
        else:
            comp_filled_points.append((column, row))

    print(comp_filled_points)
    for i in range(len(comp_filled_points)):
        mapItem[comp_filled_points[i][1]][comp_filled_points[i][0]] = "*"
                        
    return mapItem

def initGame():

    matrix = int(input("Введите размер матрицы: ") or 5)
    mapLength = range(matrix)
    mapComputer = [[' ' for i in mapLength] for y in mapLength]
    mapPlayer = [[' ' for i in mapLength] for y in mapLength]

    # начало игры
    points = int(input("Введите колличество заполняемых клеток: ") or 5)
    pointsFinded = []
    mapComputer = generateComputerMap(mapComputer, matrix, points)
    isGame = True
    showMap(mapComputer)

    while isGame:
        x = int(input("Кордината X: ") or 0)
        y = int(input("Кордината Y: ") or 0)

        if (x >= 0 and x <= matrix and y >= 0 and y <= matrix):
            if mapComputer[y][x] == "*":
                mapPlayer[y][x] = "*"
                if [y, x] not in pointsFinded:
                    pointsFinded.append([y, x])
                showMap(mapPlayer)
                print("Попадание!")
            else:
                mapPlayer[y][x] = "-"
                showMap(mapPlayer)
                print("Мимо (((")

            if (len(pointsFinded) == points):
                showMap(mapPlayer)
                print("Победа!")
                isGame = False

    restartGame = input("Заустить игру снова? (Да/Нет): ") or 'Нет'

    if restartGame != 'Нет':
        initGame()

initGame()
