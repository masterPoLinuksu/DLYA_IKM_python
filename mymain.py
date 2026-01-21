from data import FILENAME, FIELDS, data
from io_file import save_csv
from all_reports import show_report1, show_report2, show_report3
from db_menu import manage_tenants

def main_menu():
    save_csv(FILENAME, FIELDS, data)
    print(f'\nЗагружено {len(data)} воспитанников.')

    while True:
        print("ГЛАВНОЕ МЕНЮ:")
        print("1. Полный список всех квартиросъемщиков")
        print("2. Список квартиросъемщиков с льготами")
        print("3. Список квартир по диапазону общей площади")
        print("4. Редактирование квартиросъёмщиков")
        print("0. Выход")

        choice = input("Выберите пункт (0-4): ").strip()  # Пробел добавлен здесь

        if choice == '0':
            print("До свидания!")
            break
        elif choice == '1':
            print()
            show_report1(FILENAME)
        elif choice == '2':
            print()
            show_report2(FILENAME)
        elif choice == '3':
            print()
            show_report3(FILENAME)
        elif choice == '4':
            print()
            manage_tenants(FILENAME)
        else:
            print("Некорректный ввод! Введите 0-4.")
            print()
if __name__ == "__main__":
    main_menu()
