from data import FIELDS
from io_file import load_tenants, save_csv
from kit_utils import input_number
def delete_tenant(filename, surname):
    tenants = load_tenants(filename, FIELDS)
    before = len(tenants)

    tenants = [t for t in tenants if t['Фамилия'].lower() != surname.strip().lower()]

    if len(tenants) == before:
        print("Записи с такой фамилией не найдены.")
        return

    rows_to_save = [[t[f] for f in FIELDS] for t in tenants]
    save_csv(filename, FIELDS, rows_to_save)
    print(f"Удалено записей: {before - len(tenants)}")
