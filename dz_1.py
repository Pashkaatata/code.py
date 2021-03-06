# # Поменть значение переменных местами без использование третьей а == 3 b == 5
a = 3
b = 5
print(a + b - a)
print(a + b - b)

# DZ###################################################################################################################################
# 1.Напишите программу, которая спрашивает у пользователя два слова и выводит их разделёнными запятой.
def two_words(first_word=input('введите первоне слово >>>> '), second_word=input('введите второе слово >>>> ')):
    print(first_word, ",", second_word)
    return None
two_words()

# 2.Напишите программу, которая запрашивает три целых числа a, b и x и выводит True, если x лежит между a и b, иначе – False.
def print_number(a = int(input("введите первое число: ")),
                 b = int(input("введите второе число: ")),
                 x = int(input("введите третье число: "))):
    if x < a and x > b:    # if x < a < b: \ скорее всего так нужно реализовать, чуть не понял задачу.
        print(True)
    else:
        print(False)
    return None
print_number()

# 3.Напишите программу, которая решает квадратное уравнение ax^2 + bx + c = 0 Значения a, b и c вводятся с клавиатуры.\
# Для извлечения корня используйте оператор возведения в степень, а не функцию math.sqrt, чтобы получить комплексные числа в случае,\
# если подкоренное выражение отрицательно.
def kvadrat(a=int(input('первое чиисло: >>>>>')),
            b=int(input('второе число: >>>>>>')),
            c=int(input('третье число: >>>>>>'))):
    d = b ** 2 - 4 * a * c
    if d < 0:
        print('корня нет')
    elif d > 0:
        x = (-b + d ** 0.5) / 2 * a
        x1 = (-b - d ** 0.5) / 2 * a
        print(x, ",", x1)
    elif d == 0:
        x2 = -b / 2 * a
        print(x2)
    return None

result = kvadrat()

# 4.Напишите программу, которая запрашивает у пользователя радиус круга и выводит его площадь. Формула площади круга S=pi*R^2.
def radius(r = float(input("введите радиус круга: "))):
    from math import pi
    print(str(r) + str(pi * r ** 2))
    return None
radius()

# 5.Напишите программу-калькулятор, в которой пользователь сможет ввести выбрать операцию, ввести необходимые числа и получить результат.\
# Операции, которые необходимо реализовать: сложение, вычитание, умножение, деление, возведение в степень, синус, косинус и тангенс числа.
def kalkul(b=str(input('введите операцию из предложенных вариантов +  - * / ** sin cos tan  : '))):
    if b == '+':
        a = float(input('первое чиисло: '))
        c = float(input('второе число: '))
        print('Результат: ', a + c)
    elif b == '-':
        a = float(input('первое чиисло: '))
        c = float(input('второе число: '))
        print('Результат: ', a - c)
    elif b == '*':
        a = float(input('первое чиисло: '))
        c = float(input('второе число: '))
        print('Результат: ', a * c)
    elif b == '/':
        a = float(input('первое чиисло: '))
        c = float(input('второе число: '))
        print('Результат: ', a / c)
    elif b == '**':
        a = float(input('первое чиисло: '))
        c = float(input('второе число: '))
        print('Результат: ', a ** c)
    elif b == 'sin':
        from math import sin
        a = float(input('чиисло: '))
        print('Результат: ', sin(a))
    elif b == 'cos':
        from math import cos
        a = float(input('чиисло: '))
        print('Результат: ', cos(a))
    elif b == 'tan':
        from math import tan
        a = float(input('чиисло: '))
        print('Результат: ', tan(a))
    else:
        print('Вы ввели не верный символ')
    return None

kalkul()

# 6. Напишите программу, которая спрашивает у пользователя его имя, и если оно совпадает с вашим, выдаёт определённое сообщение.
NAME = 'Pavel'
def name(q_name = input('Введите имя: ')):
    if NAME == q_name:
        print('ok')
    elif NAME != q_name:
        print('Не угадал')
    return None
name()

# 7.Даны числа a и b (a < b). Выведите сумму всех натуральных чисел от a до b (включительно).
def sum_num(a = int(input('с чего начать "число": ')),
            b = int(input('чем закончить :'))):
    for i in range(a, b + 1):
        print(i)
    return i

sum_num()

# 8. Факториалом числа n называется число 𝑛!=1∙2∙3∙…∙𝑛.\
n = int(input("ведите число: "))
fact = 1
while n > 1:
    fact *= n
    n -= 1
print(fact)

# 9. Используя вложенные циклы и функции print(‘*’, end=’’), print(‘ ‘, end=’’) и print() выведите на экран прямоугольный треугольник.
def triangle(a = int(input('Какого розмера? : '))):
    for i in range(a):
        print('\\' * i)
    return None
triangle()

# 10.Функция принимает 2 параметра - высоту и ширину прямоугольника.\
# Рисует прямоугольник :)) и возвращает True если был нарисован квадрат и False - если нет.
def rectangle(width = int(input("Ширина : ")),
              height = int(input("высота : "))):
    for x in range(height):
        for y in range(width):
            print('* ', end='')

        print()
rectangle()

# 11.Создайте функцию, которая выводит приветствие для пользователя с заданным именем.\
# Если имя не указано, она должна выводить приветствие для пользователя с Вашим именем.
def name_print(name = input('Введите имя плз : ')):
    if name:
        print('Hi ' + name)
    elif name != name:
        n = 'Pavel'
        print("Hi, Im Pashka" + n)
    else:
        print('Hi Pashka')
        return None
name_print()

# 12.Фунция принимает любое число и возвращает суму всех цыфр числа.
def my_func(x):
    z = str(x)
    y = 0
    for it in z:
        print(it)
        y += int(it)
    return z

my_func(3 + 4)

# 13.ФПользователь делает вклад в размере N $ сроком на years лет под 11.5% годовых (каждый год размер его вклада увеличивается на 11.5%. Эти деньги прибавляются к сумме вклада,\
# и на них в следующем году тоже будут проценты). Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя через years лет.

# 14.Написать функцию проверки пароля пользователя при регистрации. Что она должна делать.\
# Пользователь вводит два раза пароль(стандартная регистрация)\
# Возвращает True , если пользователь ввел два раза пароль верно и есть как минимум 2(заглянуть на функции ord() и chr()) символа с большой буквы. Иначе-False.
def form_autoristion(user_password=input('pass >>>>>'),
                     sr_ps=input('pass1 >>>>>')):
    PASSWORD = 'admin'
    if user_password == PASSWORD and sr_ps == PASSWORD:
        return True
    else:
        return False

a = form_autoristion()
print(a)

# 15.Написать функцию проверки года на высокосный. Возращает True- если высокосний.
def year(years=int(input('Введите год : '))):
    if years % 4 != 0:
        print('Обычный')
    elif years % 100 == 0:
        if years % 400 == 0:
            print('Высокосный')
        else:
            print('Обычный')
    else:
        print('Высокосный')
    return None
year()
