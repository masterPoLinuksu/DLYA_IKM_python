def parse_input(raw):
    parts = raw.split()
    if not parts:
        raise ValueError("Пустая строка.")

    try:
        n = int(parts[0])
    except ValueError:
        raise ValueError(
            "Количество шариков должно быть целым числом, получено: '" + parts[0] + "'"
        )

    if n < 0:
        raise ValueError("Количество шариков не может быть отрицательным.")
    if n > 100000:
        raise ValueError("Количество шариков не должно превышать 100 000.")

    colors_raw = parts[1:]
    if len(colors_raw) != n:
        raise ValueError(
            "Ожидалось " + str(n) + " цветов, найдено " + str(len(colors_raw)) + "."
        )

    colors = []
    for token in colors_raw:
        try:
            c = int(token)
        except ValueError:
            raise ValueError(
                "Цвет должен быть целым числом, получено: '" + token + "'"
            )
        if c < 0 or c > 9:
            raise ValueError("Цвет должен быть от 0 до 9, получено: " + str(c))
        colors.append(c)

    return colors
