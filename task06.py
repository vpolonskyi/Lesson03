def in_float():
    while True:
        try:
            result = float(input("Введи число: "))
            break
        except ValueError:
            print("Это не число.")
            continue
    return result


def in_word():
    result = ""
    while len(result) == 0 or result.find(" ") != -1:
        result = input("Введи слово без пробелов: ").strip()
    return result


def is_year_leap(y):
    try:
        y = int(y)
    except ValueError:
        return None
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        return True
    else:
        return False


def triangle(x, y, z):
    try:
        x, y, z = float(x), float(y), float(z)
    except ValueError:
        return None
    if x + y > z and x + z > y and y + z > x:
        return True
    else:
        return False


def triangle_plus(x, y, z):
    try:
        x, y, z = float(x), float(y), float(z)
    except ValueError:
        return None
    if x == y == z and triangle(x, y, z):
        return "Equilateral triangle"
    elif (x == y != z or x != y == z or x == z != y) and triangle(x, y, z):
        return "Isosceles triangle"
    elif triangle(x, y, z):
        return "Versatile triangle"
    else:
        return "Not a triangle"


def distance(x1, y1, x2, y2):
    try:
        x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)
    except Exception:
        return None
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


a = in_float()
print("Вывожу число:", a)

a = in_word()
print("Вывожу слово:", a)

print("""is_year_leap("2000")""", is_year_leap("2000"))
print("""is_year_leap(/"dfd/")""", is_year_leap("dfd"))
print("is_year_leap(2000)", is_year_leap(2000))
print("is_year_leap(3)", is_year_leap(3))
print("is_year_leap(-3.4)", is_year_leap(-3.4))

print("triangle(0, 1, 1)", triangle(0, 1, 1))
print("triangle(1, -2, 2)", triangle(1, -2, 2))
print("triangle(1, 2, 2.5)", triangle(1, 2, 2.5))

print("triangle_plus(0, 0, 0)", triangle_plus(0, 0, 0))
print("triangle_plus(-1, 1, 1)", triangle_plus(-1, 1, 1))
print("triangle_plus(1, 1, 1)", triangle_plus(1, 1, 1))
print("triangle_plus(1, 2, 2)", triangle_plus(1, 2, 2))
print("triangle_plus(1, 2, 2.5)", triangle_plus(1, 2, 2.5))
print("triangle_plus(1, 2, 3)", triangle_plus(1, 2, 3))

print("distance(3, 0, -3, 0)", distance(3, 0, -3, 0))
print("distance(3, 0, 2, 0)", distance(3, 0, 2, 0))
print("distance(24, -5.4, -5, 0)", distance(24, -5.4, -5, 0))

