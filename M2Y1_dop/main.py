import discord

with open('sigma_1.jpg', 'rb') as f:
        picture = discord.File(f)
with open('sigma_2.jpg', 'rb') as f:
        picture = discord.File(f)
with open('sigma_3.jpg', 'rb') as f:
        picture = discord.File(f)
with open('sigma_4.jpg', 'rb') as f:
        picture = discord.File(f)
with open('sigma_5.jpg', 'rb') as f:
        picture = discord.File(f)
with open('sigma_6.jpg', 'rb') as f:
        picture = discord.File(f)






















## Так можно прочитать весь файл
# f = open('text.txt', 'r', encoding='utf-8')
# text = f.read()
# print(text)
# f.close()

## А так перезапишем файл полностью
# f = open('text.txt', 'w', encoding='utf-8')
# text = 'Новый текст'
# f.write(text)
# f.close()

#r’ - открывает файл только для чтения;
#‘a’ - записывает в конец файла, но не удаляет ничего из него;
#‘rb’ - открывает нетекстовый файл для чтения;
#'wb’ - открывает нетекстовый файл для записи.