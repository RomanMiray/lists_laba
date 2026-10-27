import random


def task_1():
    print("===== Задание 1 =====")
    s = input("Введите строку: ")

    while True:
        print("1 - с готовыми функциями")
        print("2 - без готовых функций")
        choice = input("Выберите способ: ")

        if choice == '1':
            count = len(s.split())
            print("Исходная строка: ", s)
            print("Количество слов: ", count)
            break
        elif choice == '2':
            count = 0
            in_word = False

            for ch in s:
                if ch != " " and ch != "\t":
                    if not in_word:
                        count += 1
                        in_word = True
                else:
                    in_word = False

            print("Исходная строка: ", s)
            print("Количество слов: ", count)
            break
        else:
            print("Неверный выбор")

def task_2():
    print("===== Задание 2 =====")

    s = input("Введите строку: ")

    while True:
        print("1 - с готовыми функциями")
        print("2 - без готовых функций")
        choice = input("Выберите способ: ")

        if choice == "1":
            result = ""
            for ch in s:
                if ch.islower():
                    result += ch.upper()
                elif ch.isupper():
                    result += ch.lower()
                else:
                    result += ch
            print("Исходная строка: ", s)
            print("Измененная строка: ", result)
            break
        elif choice == "2":
            result = ""

            lower = "abcdefghijklmnopqrstuvwxyz" + "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
            upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

            for ch in s:
                found = False
                for i in range(len(lower)):
                    if ch == lower[i]:
                        result += upper[i]
                        found = True
                        break
                    elif ch == upper[i]:
                        result += lower[i]
                        found = True
                        break
                if not found:
                    result += ch
                    
            print("Исходная строка: ", s)
            print("Измененная строка: ", result)
            break
        else:
            print("Неверный выбор")

def task_3():
    print("===== Задание 3 =====")

    while True:
        try:
            n = int(input("Введите количество элементов списка: "))
            if n > 0:
                break
            print("Количество элементов должно быть положительным.")
        except ValueError:
            print("Введите целое число.")

    print("1 — с готовыми функциями")
    print("2 — без готовых функций")
    choice = input("Выберите способ: ")

    a = [random.randint(-20, 20) for _ in range(n)]
    print("Исходный список: ", a)

    if choice == "1":
        max_index = a.index(max(a))
        a[0], a[max_index] = a[max_index], a[0]
        negative_sum = sum(x for x in a if x < 0)

        print("Преобразованный список:", a)
        print("Сумма отрицательных элементов:", negative_sum)
    elif choice == "2":
        max_index = 0
        for i in range(1, n):
            if a[i] > a[max_index]:
                max_index = i

        a[0], a[max_index] = a[max_index], a[0]

        negative_sum = 0
        for i in range(n):
            if a[i] < 0:
                negative_sum += a[i]

        print("Преобразованный список:", a)
        print("Сумма отрицательных элементов:", negative_sum)
    else:
        print("Неверный выбор способа.")

while True:
    print("============================")
    print("1. Подсчёт количества слов в строке")
    print("2. Изменение регистра букв")
    print("3. Обработка одномерного списка")
    print("0. Выход")

    choice = input("Выберите задание: ").strip()

    if choice == "1":
        task_1()
    elif choice == "2":
        task_2()
    elif choice == "3":
        task_3()
    elif choice == "0":
        print("Работа программы завершена.")
        break
    else:
        print("Нет такого пункта меню. Попробуйте ещё раз.")
