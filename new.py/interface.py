import os
from game import count_destroyed
from parser import parse_input

DIVIDER = "—" * 50


def read_choice(prompt, valid):
    while True:
        raw = input(prompt).strip()
        if raw in valid:
            return raw
        print("  [!] Допустимые варианты: 0, 1, 2, 3, 4. Попробуйте ещё раз.")


def show_result(destroyed, total):
    print()
    print("  Всего шариков : " + str(total))
    print("  Уничтожено   : " + str(destroyed))
    print("  Осталось     : " + str(total - destroyed))


def menu_manual():
    print("\n[ Ручной ввод ]")
    print("Введите количество шариков и цвета (0–9) в одну строку.")
    print("Пример:  5 1 3 3 3 2")
    while True:
        raw = input("  >> ").strip()
        if raw == "":
            print("  [!] Пустой ввод. Попробуйте ещё раз.")
            continue
        try:
            colors = parse_input(raw)
            break
        except ValueError as exc:
            print("  [!] Ошибка: " + str(exc))

    destroyed = count_destroyed(colors)
    show_result(destroyed, len(colors))


def menu_file():
    print("\n[ Загрузка из файла ]")
    print("Файл должен содержать строку вида:  N c1 c2 ... cN")
    while True:
        path = input("  Путь к файлу >> ").strip()
        if path == "":
            print("  [!] Путь не может быть пустым.")
            continue
        if not os.path.exists(path):
            print("  [!] Файл не найден: '" + path + "'")
            retry = read_choice("  Попробовать снова? (да/нет) >> ", ["да", "нет"])
            if retry == "нет":
                return
            continue
        try:
            f = open(path, "r", encoding="utf-8")
            raw = f.read().strip()
            f.close()
        except OSError as exc:
            print("  [!] Не удалось открыть файл: " + str(exc))
            return

        try:
            colors = parse_input(raw)
            break
        except ValueError as exc:
            print("  [!] Некорректные данные в файле: " + str(exc))
            return

    destroyed = count_destroyed(colors)
    show_result(destroyed, len(colors))


def menu_examples():
    examples = [
        ("5 1 3 3 3 2", 3, "Пример 1 из задания"),
        ("10 3 3 2 1 1 1 2 2 3 3", 10, "Цепная реакция 3 волн"),
        ("6 1 1 2 2 1 1", 0, "Нет цепочек >= 3"),
        ("3 5 5 5", 3, "Ровно 3 одинаковых"),
        ("1 7", 0, "Один шарик"),
        ("2 1 1", 0, "Два шарика (мало)"),
        ("8 1 1 1 2 2 2 2 1", 7, "Цепная реакция 2 волны"),
        ("5 4 4 4 4 4", 5, "Все одинаковые"),
        ("6 1 1 1 2 2 2", 6, "Две группы >= 3 рядом"),
        ("4 7 7 7 7", 4, "4 подряд"),
        ("7 3 3 3 1 3 3 3", 6, "Разделены другим цветом"),
        ("9 1 1 1 2 2 2 3 3 3", 9, "Три группы подряд"),
        ("8 1 2 1 2 1 2 1 2", 0, "Чередование без цепочек"),
        ("7 5 5 5 5 5 5 5", 7, "Все 7 одинаковые"),
    ]
    print("\n[ Встроенные примеры ]")
    i = 1
    for inp, expected, desc in examples:
        colors = parse_input(inp)
        result = count_destroyed(colors)
        if result == expected:
            status = "OK"
        else:
            status = "ОШИБКА (получено " + str(result) + ")"
        print("  " + str(i) + ") " + desc)
        print("     Вход: " + inp)
        print("     Уничтожено: " + str(result) + "  (ожидалось: " + str(expected) + ")  " + status)
        i += 1
    print()


def menu_about():
    print("\n[ О программе ]")
    print("  Задача «Шарики».")
    print("  Когда в линии образуется цепочка из 3+ одноцветных шаров,")
    print("  она уничтожается. Шары схлопываются — возможны цепные реакции.")
    print("  Программа подсчитывает суммарное число уничтоженных шаров.")
    print()
    print("  Структура данных: стек на односвязном списке (класс Stack).")
    print("  Модули: game.py (алгоритм), main.py (интерфейс).")
    print()
