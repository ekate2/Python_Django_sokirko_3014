# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Занятие 1. Задача 1
# list_ = []
# n = int(input("Введите количество элеметов списка: "))
# for i in range(n):
#     list_.append(int(input("Введите число: ")))
# for j in list_:
#     if j == 237:
#         print("В списке встретилось число 237")
#         break
#     elif j % 2 == 0:
#         print(j)
# Занятие 1. Задача 2
random_ = int(input("Введите произвольное число: "))
border_ = int(input("Введите пограничное число : "))
if random_ < border_:
    print("1-ое число меньше пограничного")
elif random_ == border_:
    print("1-ое число равно пограничному")
elif random_//border_ > 3:
    print("1-ое число больше пограничного более, чем в 3 раза")
else:
    print("1-ое число больше пограничного")
