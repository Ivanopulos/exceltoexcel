import re
import pyperclip
import pandas
#dej="ГБУЗ-МО ПОГБ ФМБА 15 +1"
#print(re.findall(r'ГБУЗ.(\w+)\s\w+\s(\w+)',dej))
a = pyperclip.paste()  # подтягиваем из буфера обмена
print(a)
b = re.split(r'\r\n', a)  # разбиваем на список
b = pandas.DataFrame(b)
b1 = b[b.columns[0]].str.split('\t', expand=True)  # разбиваем на колонки
print(b1)
pyperclip.copy(b1)  # возвращаем в буфер обмена