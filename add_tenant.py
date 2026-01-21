from data import FIELDS
from io_file import load_tenants, save_csv
from kit_utils import input_number

def is_valid_name(name):
    return name.isalpha() and name

def add_tenant(filename):
    tenants = load_tenants(filename, FIELDS)

    print("\nДобавление квартиросъёмщика")

    while True:
        fam = input("Фамилия: ").strip()
        if is_valid_name(fam):
            break
        print("Ошибка: фамилия должна содержать только буквы")

    while True:
        imya = input("Имя: ").strip()
        if is_valid_name(imya):
            break
        print("Ошибка: имя должно содержать только буквы")

    while True:
        otch = input("Отчество: ").strip()
        if is_valid_name(otch):
            break
        print("Ошибка: отчество должно содержать только буквы")

    street = input("Улица: ").strip()

    dom = input_number("Дом: ", int, min_val=1)
    kv = input_number("Квартира: ", int, min_val=1)
    floor = input_number("Этаж: ", int, min_val=0)

    total = input_number("Общая площадь: ", float, min_val=0)
    living = input_number("Жилая площадь: ", float, min_val=0, max_val=total)

    reg = input_number("Прописано: ", int, min_val=0)
    lgot = input_number("Льгота (0/1): ", int, min_val=0, max_val=1)

    row = [fam, imya, otch, street, dom, kv, floor, total, living, reg, lgot]

    tenants.append({
        'Фамилия': fam, 'Имя': imya, 'Отчество': otch, 'Улица': street,
        'Дом': dom, 'Квартира': kv, 'Этаж': floor,
        'Общая_площадь': total, 'Жилая_площадь': living,
        'Прописано': reg, 'Льгота': lgot,
        'Адрес': f"{street} {dom} {kv}"
    })

    rows_to_save = [
        [t[f] for f in FIELDS] for t in tenants
    ]
    save_csv(filename, FIELDS, rows_to_save)
    print("Запись добавлена.")
