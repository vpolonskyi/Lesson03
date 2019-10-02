while True:
    try:
        a, b = input("Введи два числа через пробел: ").split()
        break
    except Exception:
        print("Без пробела - никак")
        continue


try:
    print("Сумирую", float(a) + float(b))
except ValueError:
    print("Конкатентрую", a + b)
