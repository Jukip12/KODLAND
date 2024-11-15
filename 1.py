#By Shrot
#Discord: .shrot





#начало
print("Загрузка программы")
import random
commands = {}
commands['Вывод'] = 'Выводит пароли'
commands['Ввод'] = 'Сохранить новый пароль'
commands['Подбор'] = 'Создаёт случайный пароль'
commands['Удалить'] = 'Удаляет список'

dict = {}
dict['Джон'] = '123-1445'
dict['Кристина'] = '145-1789'
dict['Антон'] = '322-3456'
def Input():
    ############# ВВОД #############
    print("--------ПОДБОР--------")
    key = input('Какой ключ добавить?')
    value = input('Какое значение добавить этому ключу?')
    dict[key] = value
    for i in range(0, len(dict)):
        print(dict.keys()[i], '-', dict.values()[i])
    ################################

def Podbor():
    #############ПОДБОР#############
    print("--------ПОДБОР--------")
    number1 = random.randint(001, 999)
    number2 = random.randint(0001, 9999)
    number = number1+number2
    key = input('Как называется ключ?')
    dict[key] = number
    for i in range(0, len(dict)):
        print(dict.keys()[i], '-', dict.values()[i])
    ################################
    
def Delete():
    #удаление
    print("--------УДАЛЕНИЕ--------")
    for i in range(0, len(dict)):
        print(dict.keys()[i], '-', dict.values()[i])
    choose_delete = input("Какой ключ удалить")
    del dict[choose_delete]
    print("Завершено")
    




print("Добро Пожаловать в менеджер паролей")

print("--------МЕНЮ--------")

while True:
    command = input("Введите команду:")
    if command == "Вывод":
        print("   ")
        for i in range(0, len(dict)):
            print(dict.keys()[i], '-', dict.values()[i])
    
    
    
    ############# ВВОД #############
    elif command == "Ввод":
        Input()
    ################################
    
    
    
    
    ############# ПОДБОР #############
    elif command == "Подбор":
        Podbor()
    ################################
    
    elif command == "Удалить":
        Delete()
    
    
    elif command == "help":
        for i in range(0, len(commands)):
            print(commands.keys()[i], '-', commands.values()[i])


    else:
        print("Такой команды нет. Для списка команд введите help")
