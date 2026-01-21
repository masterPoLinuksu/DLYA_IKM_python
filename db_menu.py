
from add_tenant import add_tenant
from delete_tenant import delete_tenant
from edit_tenant import edit_tenant
def manage_tenants(filename):
    while True:
        print("РЕДАКТИРОВАНИЕ КВАРТИРОСЪЕМЩИКОВ:")
        print("1. Добавить квартиросъёмщика")
        print("2. Удалить по фамилии")
        print("3. Редактировать по фамилии")
        print("0. Назад")

        choice = input("Выберите пункт (0-3): ").strip()

        if choice == '0':
            break
        elif choice == '1':
            add_tenant(filename)
            input("\nНажмите Enter...")
        elif choice == '2':
            surname = input("Введите фамилию для удаления: ").strip()
            delete_tenant(filename, surname)
            input("\nНажмите Enter...")
        elif choice == '3':
            surname = input("Введите фамилию для редактирования: ").strip()
            edit_tenant(filename, surname)
            input("\nНажмите Enter...")
        else:
            print()
            print("Неверный пункт! Введите 0-3.")
