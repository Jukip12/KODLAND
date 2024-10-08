num10 = int(input("Введите десятичное число: "))
a = num10
list2 = []

while a != 0:
    a_old = a
    a = a // 2
    b = a_old % 2
    list2.append(b)


list2.reverse()
list2 = ''.join(map(str, list2))
print('Ваше двоичное число: ', list2)