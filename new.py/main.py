from interface import menu_manual, menu_file, menu_examples, menu_about, read_choice, DIVIDER


def print_header():
    print(DIVIDER)
    print("          ШАРИКИ — симулятор цепных реакций")
    print(DIVIDER)


def print_menu():
    print("\nГлавное меню:")
    print("  1. Ввести данные вручную")
    print("  2. Загрузить данные из файла")
    print("  3. Встроенные примеры")
    print("  4. О программе")
    print("  0. Выход")
    print(DIVIDER)


def main():
    print_header()
    while True:
        print_menu()
        choice = read_choice("Выберите пункт меню >> ", ["0", "1", "2", "3", "4"])
        if choice == "0":
            print("\n  До свидания!\n")
            break
        elif choice == "1":
            menu_manual()
        elif choice == "2":
            menu_file()
        elif choice == "3":
            menu_examples()
        elif choice == "4":
            menu_about()
        input("\n  Нажмите Enter, чтобы вернуться в меню...")


if __name__ == "__main__":
    main()
