#import copy
#Ввести строку, в которой записана сумма натуральных чисел, например, ‘1+25+3’.\
#Вычислите это выражение. Работать со строкой, как со списком.
# str_list = list(input('ввести строку, к примеру: 1+25+1 >>> '))
#
# num = 0
# sum_ = 0
# for i in str_list:
#     if i.isdigit():
#         num = int(str(num) + i)
#     else:
#         sum_ = sum_ + num
#         num = 0
# else:
#     sum_ = sum_ + num
#
# print('результат', sum_)

# Дан список из 5 различных элементов. Используя функции (не использовать цикл), необходимо найти и вывести:
# минимальный и максимальный элементы списка;
# сумму и среднее арифметическое;
# второй минимальный элемент (второй по минимальности).
# def fu(list_):
#         return min(list_), max(list_), sum(list_), sum(list_) / len(list_), sorted(list_)[1:2]
# print(fu(list_ = [1, 2, 3, 4, 5]))

# Проверить, является ли заданное слово палиндромом.
# Примечание:
# Пример палиндрома: казак, ABBA
# Использовать функции.
# Поскольку при присваивании одного списка другому, изменение первого ведет к аналогичному изменению второго списка, то необходимо использовать копию (copy).
# def palindrome(s=[]):
#     l = len(s)
#     for i in range(l//2):
#         if s[i] != s[-1-i]:
#             print("не палиндрома")
#         quit()
#         print("палиндрома")
#     return s
# palindrome('казак, ABBA')
#Найдите в списке все простые числа и скопируйте их в новый список.
# def funct_cpy(a=[]):
#     for i in range(len(a)):
#         if 0 <= i <= 9:
#             new_list = copy.copy(a)
#     return new_list
# print(funct_cpy([1, 2, 3, 4, 5]))

#Найти среднее арифметическое всех элементов списка.
# def ar(args=[]):
#     return sum(args) / len(args)
# print(ar([1, 2, 3]))
#Запросить у пользователя элемент списка и вывести его индекс.
# def choice_index(elem=input("value, drop index [1, 2, 3, 4, 5] :>>>>>>>>")):
#     lst = ["1", "2", "3", "4", "5"]
#     for item in lst:
#         if item == elem:
#             return lst.index(item)
#         else:
#             print("is not value in list")
#             break
# print("index :", choice_index())
