from data import FIELDS
def save_csv(filename, fields, rows):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(';'.join(fields) + '\n')
        for row in rows:
            f.write(';'.join(str(x) for x in row) + '\n')

def load_tenants(filename, fields):
    tenants = []
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()
    if not lines:
        return tenants
    for line in lines[1:]:
        parts = line.split(';')
        if len(parts) != len(fields):
            continue
        row = {}
        for i in range(len(fields)):
            row[fields[i]] = parts[i]
        row['Дом'] = int(row['Дом'])
        row['Квартира'] = int(row['Квартира'])
        row['Этаж'] = int(row['Этаж'])
        row['Общая_площадь'] = float(row['Общая_площадь'])
        row['Жилая_площадь'] = float(row['Жилая_площадь'])
        row['Прописано'] = int(row['Прописано'])
        row['Льгота'] = int(row['Льгота'])
        row['Адрес'] = f"{row['Улица']} {row['Дом']} {row['Квартира']}"
        tenants.append(row)
    return tenants