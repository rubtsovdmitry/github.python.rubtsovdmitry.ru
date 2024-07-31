"""ПРОГРАММА СЧИТАЕТ КОЛИЧЕСТВО ПРОГРАММ, ОПУБЛИКОВАННЫХ НА САЙТЕ. ВЫБИРАЕТ ТОЛЬКО ПОДХОДЯЩИЕ ФАЙЛЫ."""

import pathlib, os, shelve


# ! КОСТЫЛЬ
"""посчитаем количество файлов, которые нужны, но в них нет "task"""
def second():
    a = pathlib.Path.cwd()                                          # текущее расположение, объект Pathlib
    b = os.listdir(a)                                               # список всего содержимого текущего каталога в список
    count = 0
    for i in b:        
        if os.path.isfile(i):                                       # если содержимое каталога является файлом, то выводим на печать
            if "graphs.html" not in i and\
               "greed.html" not in i and\
               "recursion.html" not in i: 
                count += 1       
    return count                                                          # базовым случаем является самый нижний каталог, в котором не окажется других каталогов и тем самым код функции закончится и вызовет возврат стека


"""посчитаем количество файлов, в названии которых есть "task"""
def first():
    a = pathlib.Path.cwd()  # текущее расположение, объект Pathlib
    b = os.listdir(a)  # список всего содержимого текущего каталога в список
    count = 0
    for i in b:  # обходим содержимое каталога
        x = str(a / i)  # полный путь к элементу в цикле
        if os.path.isfile(x):  # копим счётчик при условии
            if "task" in x:
                count += 1
        else:  # если содержимое каталога является каталогом, то проваливаемся в него и рекурсивно запускам текщую функция
            os.chdir(a / i)
            count += first()        
    return count  # базовым случаем является самый нижний каталог, в котором не окажется других каталогов и тем самым код функции закончится и вызовет возврат стека


start = str(pathlib.Path.cwd())  # запомним первоначальный каталог (это каталог с py-скриптами)
os.chdir("..")  # перейдём в корневой каталог сайта
first_part = first()  # <-- посчитаем количество файлов, в названии которых есть "task"
os.chdir(start)  # попадём в первоначальный каталог
os.chdir("../content/4_algorithms")  # ! <-- попадём в каталог, в котором искомые файлы не имеют слова "task", не стал менять структура сайта, где все названия содержат "task" и сделал такой КОСТЫЛЬ
second_part = second()  # <-- посчитаем количество файлов, которые нам нужны

result = first_part + second_part  # количество искомых файлов
print(result)