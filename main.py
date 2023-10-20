import random
import re

# a = input('Введите первое число\n')
# b = input('Введите второе число\n')
# c = input('Введите третье число\n')
#
# if a < b and b < c:
#     print(b, 'среднее')
# elif b > c and c < a:
#     print(a, 'среднее')
# else: print(a, 'среднее') #можно не делать третье условие а сразу вывод


# arr = []
# arr2 = []
# limit = 0

# # 1. Создаем список с тремя случайными числами от 0 до 10.
# for i in range(0,3):
#     arr.append(random.randint(0,10))
# print(arr)

# 2. Написать цикл, в котором будут выводиться в консоль уникальные номера каждого элемента данного списка
# (из первой задачи список)


# for i in arr: print(id(arr))
# # size = 1
# spl_list = list()
# for i in range(0, len(arr), size):
#     spl_list.append(arr[i:i+size])
# print(spl_list)


# arr = [int(i) for i in input().split()]
# for i in arr:
#    if arr.count(i) == 1:
#        print(i)

# for i in str(arr):
#     if i.isnumeric():
#         print(id(i))
#
#
# arr = '123abc'
# for i in arr:
#     if re.match('\d', i):
#         print(id(i))



# for i in arr:
#     if isinstance(i, int):
#         print(id(i))



# for i in range(len(arr)):
#     if type(arr[i]) == int:
#         print(id(arr[i]))

# 3. Написать цикл while на 5 итераций, который при каждой итерации запрашивает пользовательский ввод и
# записывает полученное значение в список.
# Отсортировать полученный список по длине и вывести в консоль.

# while limit < 5:
#     arr2.append(input('Введите число\n'))
#     limit += 1
#     arr2.sort()
# print(arr2)

# Создаем пустой список
# my_list = []
#
# # Цикл while с 5 итерациями
# i = 0
# while i < 5:
#     # Запрашиваем пользовательский ввод
#     user_input = input("Введите значение: ")
#
#     # Добавляем полученное значение в список
#     my_list.append(user_input)
#
#     i += 1
#
# # Сортируем список по длине элементов
# my_list.sort(key=len)
#
# # Выводим отсортированный список в консоль
# for item in my_list:
#     print(item)

#Дз
# Запрашивается пользовательский ввод, содержащий как буквы, так и числа.
# Создать вложенный список. Числа из полученной строки добавить во вложенный список.
# Список перевернуть и вывести его идентификатор.


# arr_list = input('Введите данные\n')
# arr_list2 = []
# print('Введенные данные ',arr_list)
# for i in arr_list:
#     if type(i) is int:
#         arr_list2.append(arr_list)
# print(arr_list2)

# user_input = input("Введите строку, содержащую буквы и числа:\n")
# numbers = []
# strings = []
#
# for char in user_input:
#     if char.isdigit():
#         numbers.append(int(char))
#
# numbers.reverse()
# strings.append(numbers)
# print(strings)
# print(id(numbers))



# d = ({i: random.uniform(5, 20) for i in range(5)} #создаем словарь с помощью генератора словарей
# print(d)
# #пример вывода: {0: 87, 1: 89, 2: 95, 3: 65, 4: 44, 5: 87, 6: 46, 7: 20, 8: 14, 9: 56}

# d = dict(zip(['hi', 'lo', 99], [55,True, (2,4)])) #создаем словарь с использованием zip и dict
# print(d)
# d2 = dict(zip([1, 'lo', 99], [522,'asas', (20,4)])) #создаем словарь с использованием zip и dict
# print("d2: ", d2)
# d.clear() #очищаем словарь d
# d3 = d2.copy() #копируем словарь
# print(d3.keys()) #выводим все ключи словаря d3
# print(d3.values()) #выводим все значения словаря d3
# for k,v in d3.items(): #проходимся по парам словаря d3
#     if type(k) == int: #проверяем, является ли ключ числом
#         del d2[k] #удаляем пару по ключу, который является числом
# print("d2: ", d2) #вывод словаря d2

# ДЗ: Два раза запросить пользовательский ввод. Обернуть их в множество, найти пересечения и на их основе с
# помощью dict.fromkeys создать словарь, где значениями указать строку test. Получившийся словарь вывести в консоль.


# ДЗ: Два раза запросить пользовательский ввод. Обернуть их в множество, найти пересечения и на их основе с
# помощью dict.fromkeys создать словарь, где значениями указать строку test. Получившийся словарь вывести в консоль.

# a_input = input('Введите данные разделенные пробелом, первый раз \n')
# b_input = input('Введите данные разделенные пробелом, второй раз \n')
# user_list1 = set(a_input.split())
# user_list2 = set(b_input.split())
# user_set = user_list1 & user_list2
# user_dict = dict.fromkeys(user_set, 'test')
#
# print(type(user_set), user_set)
# print(user_dict)


# s = [set(input()) for i in range(2)]
# print(dict.fromkeys(s[0] & s[1], 'test'))
#
# try:
#     a = int(input("Введите число\n"))
#     b = int(input("Введите число\n"))
#     print(a/b)
# except (ValueError, ArithmeticError) as e: print("Ошибка следующая: ",e)
# else:
#     print((a/b)**2)
# finally: print('задача finalli выполнена ')


# a = ['sdf', 'qwe', 'zxc', 'afd', 'rew', random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)]
# print(a)
# for i in a:
#     try: print(float(i))
#     except ValueError: print("Ошибка перевода!")

# try: a = input('Введите данные \n')
# except KeyboardInterrupt: print('Не верно')

# arr = ['dvsd', 2, 'Dsv']
# d = {}
# for i in arr: d[str(i)] = random.uniform(100, 999)
# try: print(d[input('введите ключ\n')])
# except: print('Нет такого ключа')


# class Computer():
#   def __init__(self, computer, ram, ssd):
#     self.computer = computer
#     self.ram = ram
#     self.ssd = ssd
#
# class Laptop(Computer):
#   def __init__(self, computer, ram, ssd, model):
#     super().__init__(computer, ram, ssd)
#     self.model = model
#
# lenovo = Laptop('lenovo', 2, 512, 'l420')
# print('This computer is:', lenovo.computer)
# print('This computer has ram of', lenovo.ram)
# print('This computer has ssd of', lenovo.ssd)
# print('This computer has this model:', lenovo.model)

# Задача 1:

import os
# Создание папки
os.mkdir("papka")
# Переход в папку
os.chdir("papka")
# Создание пайтон-файла и запись имени в него
with open("my_name.py", "w") as file:
    file.write('print("Pavel")')

# Задача 2:

def decorator(func):
    def wrapper():
        print("Декоратор использован")
        func()
    return wrapper
@decorator
def name():
    print("Pavel")
@decorator
@decorator
def surname():
    print("Polivoda")
# Вызов декорируемых функций
name()
surname()

# Задача 3:

from abc import ABC, abstractmethod
# Абстрактный класс
class AbstractClass(ABC):
    @abstractmethod
    def method1(self):
        pass
    @abstractmethod
    def method2(self):
        pass
    @abstractmethod
    def method3(self):
        pass
# Второй класс, наследник от первого
class SecondClass(AbstractClass):
    def method1(self):
        print("Method 1")
    def method2(self):
        print("Method 2")
    def method3(self):
        print("Method 3")
    @staticmethod
    def dop_method():
        print("Additional Method")
# Создание экземпляра второго класса
second_obj = SecondClass()

# Запуск всех методов
second_obj.method1()
second_obj.method2()
second_obj.method3()
SecondClass.dop_method()