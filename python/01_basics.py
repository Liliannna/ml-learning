#Использование Python как калькулятор
print("2+2=", 2+2)
print("50-5*6=", 50-5*6)
print("(50-5*6)/4 = ", (50-5*6)/4)
print("8/5 = ", 8/5)
print(17/3)
print(17//3)
print(17%3)
print(5*3+2)
print(5**2)
print(2**7)
width = 20
height = 5*9
print(width*height)
print(4*3.75-1)
tax = 12.5 / 100
price = 100.50
print(price * tax)

#Текст
print('спам яйца')
print("Парижский кролик тебя прикроет :)! Ура!")
print('1925')
print('doesnt\'t')
print("doesn't")
print('"Yes," they said')
print("\"Yes,\" they said")
print('"Ins\'t," they said')
s = 'Первая строка. \nВторая строка.'
print(s)
print('C:\this\name')
print(r'C:\this\name')
print("""\
    Usage: thingy [OPTIONS]
        -h                       Показать это сообщение о применении
        -H hostname              Имя хоста для подключения
    """)
print(3*'un'+'ium')
print('Py' 'thon')
text = ('Поместите несколько строк в круглые скобки, '
        'чтобы они были объеденены вместе.')
print(text)
prefix = 'Py'
print(prefix + 'thon')
word = 'Python'
print(word[0])
print(word[5])
print(word[-1])
print(word[-2])
print(word[-6])
print(word[0:2])
print(word[2:5])
print(word[:2])
print(word[4:])
print(word[-2:])
print(word[:2]+word[2:])
print(word[:4]+word[4:])
print('J'+word[1:])
print(word[:2]+'py')
s = 'ghkkhmfgkhmfkgkftflkt'
print(len(s))

#Списки
squares = [1, 4, 9, 16, 25]
print(squares)
print(squares[0])
print(squares[-1])
print(squares[-3:])
print(squares + [36, 49, 64, 81, 100])
cubes = [1, 8, 27, 65, 125]
print(cubes)
cubes[3] = 64
print(cubes)
cubes.append(216)
cubes.append(7**3)
print(cubes)
rgb = ["Red", "Green", "Blue"]
rgba = rgb
print(id(rgb) == id(rgba))
rgba.append("Alph")
print(rgb)
correct_rgba = rgba[:]
correct_rgba[-1] = "Alpha"
print(correct_rgba[-1])
print(rgba)
print(correct_rgba)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
letters[2:5] = ['C', 'D', 'E']
print(letters)
letters[2:5] = []
print(letters)
letters[:] = []
print(letters)
letters = ['a', 'b', 'c', 'd']
print(len(letters))
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])

#Первые шаги в программировании
# Ряд Фибоначчи:
# сумма двух элементов определяет следующий
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

#Инструкция if
x = int(input("Пожалуйста введите целое число: "))

if x < 0:
    x = 0
    print('Отрицательное числе заменено нулем')
elif x==0:
    print('Ноль')
elif x==1:
    print('Единица')
else:
    print('Больше единицы')

#Инструкция for
words = ['кот', 'окно', 'выбросить']
for w in words:
    print(w, len(w))


users = {'Hans': 'активен', 'Éléonore': 'неактивна', '景太郎': 'активен'}

for user, status in users.copy().items():
    if status == "неактивна":
        del users[user]

print(users)

users = {'Hans': 'активен', 'Éléonore': 'неактивна', '景太郎': 'активен'}
active_users ={}
for user, status in users.items():
    if status == 'активен':
        active_users[user] = status

print(active_users)

#Функция range()
for i in range(5):
    print(i)

print(list(range(5,10)))
print(list(range(0,10,3)))
print(list(range(-10, -100, -30)))
print(list(range(-100, -30, 30)))

a = ['У', 'Мэри', 'была', 'маленькая', 'Собачка']
for i in range(len(a)):
    print(i, a[i])

print(sum(range(4)))

#Инструкции break и continue
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break

for num in range(2, 10):
    if num % 2 == 0:
        print(f"Найдено четное число {num}")
        continue
    print(f"Найдено нечетное числено {num}")

#else ветви в циклах
for n in range (2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'равно', x, '*', n//x)
            break
    else:
        #  цикл завершился, не найдя делителя
        print(n, '- простое число')

#форматирование строк
print('{2}, {0}, {1}'.format('a', 'b', 'c'))

print('Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W'))

coord = {'latitude':'37.24N', 'longitude':'-115.81W'}
print('Coordinates: {latitude}, {longitude}'.format(**coord))

print("Unit destroyed: {players[0]}".format(players = [1, 2,3]))
print("Unit destroyed: {players[0]!r}".format(players = [1, 2,3]))

coord = (3, 5)
print('X: {0[0]}; Y: {0[1]}'.format(coord))

print("rerp() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2'))

print('{:<30}'.format('left aligned'))
print('{:>30}'.format('right aligned'))
print('{:^30}'.format('centered'))
print('{:*^30}'.format('centered'))
print('{:+f}; {:+f}'.format(3.14, -3.14))
print('{: f}; {: f}'.format(3.14, -3.14))
print('{:-f}; {:-f}'.format(3.14, -3.14))
print('int: {0:d}; hex: {0:x}; oct: {0:o}; bin: {0:b}'.format(42))
print('int: {0:d}; hex: {0:#x}; oct: {0:#o}; bin: {0:#b}'.format(42))

points = 19.5
total = 22
print('Correct answers: {:.2%}'.format(points/total))

print('Hello, %s!' % 'Vasya')
print('%d %s, %d %s' % (6, 'bananas', 10, 'lemons'))
print('%(languages)s has %(number)03d quote types.'%{"languages":"Python", "number":2})

print('%.2s' % 'Hello!')
print('%.*s' % (2, 'Hello!'))
