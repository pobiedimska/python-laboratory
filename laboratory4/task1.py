import math
global triangle

def add_point(triangle, point_number=0):
    e = 0
    new_point = [" ", " "]
    while new_point[0].isprintable() and new_point[1].isprintable():
        if not point_number == 0:
            new_point = input('Введіть координати х' + str(point_number) + ', y' + str(point_number) +
                              ' вершини  трикутника через кому').replace(" ", "").split(',')
        else:
            new_point = input('Введіть координати х, y точки у середині трикутника через кому').replace(" ", "").split(
                ',')
        for j in range(len(new_point)):
            try:
                if not len(new_point) == 2:
                    raise Exception
                new_point[j] = float(new_point[j].rstrip())
                e = 0
            except (ValueError, TypeError, Exception):
                print('Для таких значень неможливо вирішити задачу, спробуйте інше')
                new_point = [" ", " "]
                e = 1
                break
            continue
        if e != 1:
            break
        continue
    if not point_number == 0:
        triangle.append(new_point)
    else:
        if len(triangle) < 4:
            triangle.append(new_point)
        else:
            triangle[3] = new_point


def check(points_list, triger=0):
    # якщо перевіряємо площу, то тригер буде 0, а якщо шукаємо найменшу відстань, но 1
    area = []
    distance = []

    side1 = math.sqrt((points_list[0][0] - points_list[1][0]) ** 2 + (points_list[0][1] - points_list[1][1]) ** 2)
    side2 = math.sqrt((points_list[1][0] - points_list[2][0]) ** 2 + (points_list[1][1] - points_list[2][1]) ** 2)
    side3 = math.sqrt((points_list[2][0] - points_list[0][0]) ** 2 + (points_list[2][1] - points_list[0][1]) ** 2)
    p1 = (side1 + side2 + side3) / 2
    ar1 = math.sqrt(abs(p1 * (p1 - side1) * (p1 - side2) * (p1 - side3)))
    area.append(ar1)

    for a in range(3):
        side1 = math.sqrt((points_list[a][0] - points_list[(a + 1) % 3][0]) ** 2
                          + (points_list[a][1] - points_list[(a + 1) % 3][1]) ** 2)
        side2 = math.sqrt((points_list[a][0] - points_list[3][0]) ** 2
                          + (points_list[a][1] - points_list[3][1]) ** 2)
        side3 = math.sqrt((points_list[3][0] - points_list[(a + 1) % 3][0]) ** 2
                          + (points_list[3][1] - points_list[(a + 1) % 3][1]) ** 2)
        p = (side1 + side2 + side3) / 2
        ar = round(math.sqrt(p * (p - side1) * (p - side2) * (p - side3)), 2)
        d = round(ar * 2 / side1, 2)
        area.append(ar)
        distance.append(d)

    if triger == 0:
        if area[1] + area[2] + area[3] > area[0]:
            return True
        return False
    else:
        distance.sort()
        return str(round(distance[0], 2))


print("Побєдімська Соня Ігорівна\nЛабораторна робота №4\nВаріант 17\nЗнаходження відстані від точки до найближчої сторони\n")
triangle = []
other = ""
for i in range(3):
    add_point(triangle, i + 1)
while other == "":
    add_point(triangle)
    while check(triangle):
        print("Точка знаходиться за межами трикутника. Введіть інше значення точки")
        add_point(triangle)
    print("Відстань від точки до найближчої сторони дорівнює " + check(triangle, 1))
    other = input("Перевірити іншу точку? Введіть будь-що для завершення або натисніть ENTER для продовження")
