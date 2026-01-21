def input_number(prompt, cast=float, min_val=None, max_val=None):
    while True:
        s = input(prompt).strip().replace(',', '.')
        try:
            val = cast(s)
        except ValueError:
            print("Введите корректное число!")
            continue
        if min_val is not None and val < min_val:
            print(f"Значение должно быть >= {min_val}")
            continue
        if max_val is not None and val > max_val:
            print(f"Значение должно быть <= {max_val}")
            continue
        return val

def print_header():
    print("ФИО            | Адрес       | Этаж | Площадь | Проп. | Льг")


def shell_sort(records, key_funcs, descending=None):
    if descending is None:
        descending = [False] * len(key_funcs)
    n = len(records)
    gap = 1
    while gap < n // 3:
        gap = 3 * gap + 1
    while gap > 0:
        for i in range(gap, n):
            temp = records[i]
            j = i
            while j >= gap:
                cmp = 0
                for k_idx, key_func in enumerate(key_funcs):
                    val1 = key_func(temp)
                    val2 = key_func(records[j - gap])
                    if val1 != val2:
                        if descending[k_idx]:
                            cmp = -1 if val1 > val2 else 1
                        else:
                            cmp = -1 if val1 < val2 else 1
                        break
                if cmp >= 0:
                    break
                records[j] = records[j - gap]
                j -= gap
            records[j] = temp
        gap //= 3
    return records