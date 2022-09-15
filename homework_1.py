# Задача № 1

""" count = int(input('Введиете порядковые номер дня недели: '))
if count > 7:
    print('Данного дня недели не существует!')
elif count <=5:
    print('NO')
else:
    print("YES") """


#Задача №2
""" 
def inputNumbers(x):
    xyz = ["X", "Y", "Z"]
    a = []
    for i in range(x):
        a.append(input(f"Введите значение {xyz[i]}: "))
    return a
def checkPredicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result
statement = inputNumbers(3)
if checkPredicate(statement) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")
 """

#Задача № 3
""" 
def inputKoord(x):
    a = [0] * x
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = float(input(f"Введите {i+1} координатину: "))
                a[i] = number
                is_OK = True
                if a[i] == 0:
                    is_OK = False
                    print("Координатина не должна быть равна 0 ")
            except ValueError:
                print("Ты как бы ошибся. Вводить надо исключительно числа!")
    return a
def checkCoordinates(xy):
    text = 4
    if xy[0] > 0 and xy[1] > 0:
        text = 1
    elif xy[0] < 0 and xy[1] > 0:
        text = 2
    elif xy[0] < 0 and xy[1] < 0:
        text = 3
    print(f"Точка находится в {text} четверти плоскости")
koordinate = inputKoord(2)
checkCoordinates(koordinate)
 """
# Задача № 4
"""koordinate = int(input('Введите номер четверти (от 1 до 4): '))
if (koordinate > 4):
    print('Попробуй все таки еще раз прчитать условие! Не больше 4-х!!!')
else:
    if koordinate == 1:
        print('координаты x от 0 до + бесконечности')
        print('координаты y от 0 до + бесконечности')
    elif koordinate == 2:
        print('координаты x от 0 до - бесконечности')
        print('координаты y от 0 до + бесконечности')
    elif koordinate == 3:
        print('координаты x от 0 до - бесконечности')
        print('координаты y от 0 до - бесконечности')
    elif koordinate == 4:
        print('координаты x от 0 до + бесконечности')
        print('координаты y от 0 до - бесконечности')
 """

# Задача № 5
def inputNumbers(x):
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = int(input(f"Введите координату по {xy[i]}: "))
                a.append(number)
                is_OK = True
            except ValueError:
                print("Ты ошибся. Вводить надо именно целые числа!")
    return a
def calcLengthSegments(a, b):
    lengthSegments = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return lengthSegments
print("Введите координаты точки А")
pointA = inputNumbers(2)
print("Введите координаты точки В")
pointB = inputNumbers(2)
print(f"Длина отрезка: {format(calcLengthSegments(pointA, pointB), '.2f')}")
