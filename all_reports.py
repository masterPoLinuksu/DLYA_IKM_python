from data import FIELDS
from io_file import load_tenants
from kit_utils import input_number, print_header, shell_sort

def show_report1(filename):
    print("\n ОТЧЕТ 1: Полный список ")
    print("Сортировка: кол-во прописанных (убывание) + адрес (возрастание)")
    tenants = load_tenants(filename, FIELDS)
    key_funcs = [lambda t: t['Прописано'], lambda t: t['Адрес']]
    desc = [True, False]
    report = shell_sort(tenants.copy(), key_funcs, desc)
    print_header()
    for t in report:
        print(f"{t['Фамилия']} {t['Имя'][:1]}.{t['Отчество'][:1]}. | {t['Адрес']} | эт.{t['Этаж']} | пл.{t['Общая_площадь']:.1f} | проп.{t['Прописано']} | льг:{t['Льгота']}")
    input("\nНажмите Enter для возврата в меню...")

def show_report2(filename):
    print("\n ОТЧЕТ 2: Со льготами ")
    print("Сортировка: этаж (возрастание) + прописанные (убывание) + общая площадь (возрастание)")
    tenants = load_tenants(filename, FIELDS)
    tenants_lgot = [t for t in tenants if t['Льгота'] == 1]
    if not tenants_lgot:
        print("Нет записей с льготами.")
        input("\nНажмите Enter...")
        return
    key_funcs = [lambda t: t['Этаж'], lambda t: t['Прописано'], lambda t: t['Общая_площадь']]
    desc = [False, True, False]
    report = shell_sort(tenants_lgot.copy(), key_funcs, desc)
    print_header()
    for t in report:
        print(f"{t['Фамилия']} {t['Имя'][:1]}.{t['Отчество'][:1]}. | {t['Адрес']} | эт.{t['Этаж']} | пл.{t['Общая_площадь']:.1f} | проп.{t['Прописано']}")
    input("\nНажмите Enter для возврата в меню...")

def show_report3(filename):
    print("\n ОТЧЕТ 3: По диапазону площади ")
    print("Сортировка: льгота (возрастание) + общая площадь (убывание)")
    N1 = input_number("Минимальная площадь (кв.м.): ", float)
    N2 = input_number("Максимальная площадь (кв.м.): ", float, min_val=N1)
    tenants = load_tenants(filename, FIELDS)
    tenants_area = [t for t in tenants if N1 <= t['Общая_площадь'] <= N2]
    if not tenants_area:
        print(f"Нет квартир с площадью {N1}-{N2} кв.м.")
        input("\nНажмите Enter...")
        return
    key_funcs = [lambda t: t['Льгота'], lambda t: t['Общая_площадь']]
    desc = [False, True]
    report = shell_sort(tenants_area.copy(), key_funcs, desc)
    print("ФИО           | Адрес      | Площадь | Льг")
    for t in report:
        print(f"{t['Фамилия']} {t['Имя'][:1]}.{t['Отчество'][:1]}. | {t['Адрес']} | пл.{t['Общая_площадь']:.1f} | льг:{t['Льгота']}")
    input("\nНажмите Enter для возврата в меню...")