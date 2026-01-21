from data import FIELDS
from io_file import load_tenants, save_csv
from kit_utils import input_number

def is_valid_name(name):
    return name and all(c.isalpha() for c in name)

def edit_tenant(filename, surname):
    tenants = load_tenants(filename, FIELDS)
    surname_norm = surname.strip().lower()

    matches = [i for i, t in enumerate(tenants) if t['Фамилия'].lower() == surname_norm]
    if not matches:
        print("Записи с такой фамилией не найдены.")
        return

    if len(matches) > 1:
        print("\nНайдено несколько записей:")
        for n, idx in enumerate(matches, start=1):
            t = tenants[idx]
            print(f"{n}) {t['Фамилия']} {t['Имя']} {t['Отчество']} | {t['Адрес']}")
        pick = input_number("Выберите номер записи: ", int, min_val=1, max_val=len(matches))
        target_idx = matches[pick - 1]
    else:
        target_idx = matches[0]

    t = tenants[target_idx]
    print("\nРедактирование (Enter = оставить без изменений)")

    def ask_str(field):
        while True:
            new_val = input(f"{field} [{t[field]}]: ").strip()
            if new_val == "":
                return t[field]
            if field in ['Фамилия', 'Имя', 'Отчество'] and not is_valid_name(new_val):
                print(f"Ошибка: {field} должна содержать только буквы")
                continue
            return new_val

    def ask_int(field, min_val=None, max_val=None):
        s = input(f"{field} [{t[field]}]: ").strip()
        if s == "":
            return t[field]

        if field in ['Дом', 'Квартира']:
            if int(s) <= 0:
                print(f"Ошибка: {field} должно быть положительным числом")
                return ask_int(field, min_val, max_val)

        return input_number(f"Введите {field}: ", int, min_val=min_val, max_val=max_val)

    def ask_float(field, min_val=None, max_val=None):
        s = input(f"{field} [{t[field]}]: ").strip()
        if s == "":
            return t[field]
        return input_number(f"Введите {field}: ", float, min_val=min_val, max_val=max_val)

    t['Фамилия'] = ask_str('Фамилия')
    t['Имя'] = ask_str('Имя')
    t['Отчество'] = ask_str('Отчество')
    t['Улица'] = ask_str('Улица')

    t['Дом'] = ask_int('Дом', min_val=1)
    t['Квартира'] = ask_int('Квартира', min_val=1)
    t['Этаж'] = ask_int('Этаж', min_val=0)

    t['Общая_площадь'] = ask_float('Общая_площадь', min_val=0)
    t['Жилая_площадь'] = ask_float('Жилая_площадь', min_val=0, max_val=t['Общая_площадь'])

    t['Прописано'] = ask_int('Прописано', min_val=0)
    t['Льгота'] = ask_int('Льгота', min_val=0, max_val=1)

    t['Адрес'] = f"{t['Улица']} {t['Дом']} {t['Квартира']}"

    rows_to_save = [[x[f] for f in FIELDS] for x in tenants]
    save_csv(filename, FIELDS, rows_to_save)
    print("Запись обновлена.")