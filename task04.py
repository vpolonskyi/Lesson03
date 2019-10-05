lin = []
while True:
    if lin == []:
        lin = input("Введите список чисел: ")
        s_lin = lin
        lin = lin.replace(",", " ").split()
    else:
        break

    for i in range(len(lin)):
        try:
            lin[i] = float(lin[i])
        except ValueError:
            print("Я же просил список чисел!", lin[i], "- не число!")
            lin = []
            break

d_lin = lin.copy()
print("Выводжу на экран и удаляю, с начала, элементы списка: ", d_lin)
while d_lin:
    print(d_lin.pop(0))
print("Теперь в списке осталось: ", d_lin)

d_lin = s_lin
print("Выводжу на экран и удаляетю первый символ строки, пока строка", d_lin, "не станет пустой")
while d_lin:
    print(d_lin)
    d_lin = d_lin[1:]
print("Теперь в строке осталось: ", d_lin)

d_lin = lin.copy()
print("Выводжу на экран и удаляю элементы списка", d_lin, "от самого маленького до самого большого")
d_lin.sort()
while d_lin:
    print(d_lin[0])
    d_lin = d_lin[1:]
print("Теперь в списке осталось: ", d_lin)

d_lin = lin.copy()
print("Выводжу на экран и удаляю элементы несортированного списка", d_lin, "от самого маленького до самого большого")
while d_lin:
    min_lin = d_lin[0]
    for i in range(len(d_lin)):
        if min_lin > d_lin[i]:
            min_lin = d_lin[i]
    print(min_lin)
    try:
        d_lin.remove(min_lin)
    except ValueError:
        break
print("Теперь в списке осталось: ", d_lin)

d_lin = lin.copy()
for i in range(len(d_lin)):
    if d_lin[i] <= 0:
        d_lin[i] = 0
    else:
        d_lin[i] = int(d_lin[i])

while True:
    try:
        d_lin.remove(0)
    except ValueError:
        break

d_lin.append(0)

print("Дана последовательность натуральных ненулевых чисел, завершающаяся числом 0")
print(d_lin)
mx = [1]
for i in range(len(d_lin)-1):
    if d_lin[i] == d_lin[i+1]:
        mx[i:i+1] = [mx[i], mx[i]+1]
    else:
        mx[i:i+1] = [mx[i], 1]

mxx = mx.copy()
mx.sort(reverse=True)
print("Наибольшее число подряд идущих элементов этой последовательности равных друг другу", mx[0])
print("И это", d_lin[mxx.index(mx[0])+1-mx[0]:mxx.index(mx[0])+1])
