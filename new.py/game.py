from stack import Stack


def build_groups(colors):
    groups = []
    for c in colors:
        if len(groups) > 0 and groups[-1][0] == c:
            groups[-1][1] += 1
        else:
            groups.append([c, 1])
    return groups


def collapse(groups):
    for i in range(len(groups)):
        if groups[i][1] >= 3:
            destroyed = groups[i][1]
            del groups[i]
            if i > 0 and i < len(groups) and groups[i - 1][0] == groups[i][0]:
                groups[i - 1][1] += groups[i][1]
                del groups[i]
            return destroyed
    return 0


def count_destroyed(colors):
    groups = build_groups(colors)
    destroyed = 0
    while True:
        round_destroyed = collapse(groups)
        if round_destroyed == 0:
            break
        destroyed += round_destroyed
    return destroyed
