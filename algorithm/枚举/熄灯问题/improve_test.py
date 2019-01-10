a = [
    [True, True, True, True, True, True],
    [True, True, True, True, True, True],
    [True, True, True, True, True, True],
    [True, True, True, True, True, True],
    [True, True, True, True, True, True]
]


def take_action(status, actions, line):
    for i in range(0, 6):
        if status[line][i]:
            actions[line + 1][i] = True
            status = changeStatus(status, line + 1, i)
        else:
            actions[line + 1][i] = False

    if line == 3:
        for n in status[4]:
            if n:
                return False
        print("after status: ")
        print(status)
        print("actions:")
        return actions
    else:
        return take_action(status, actions, line + 1)


def changeStatus(status, point_x, point_y):
    status[point_x][point_y] = not status[point_x][point_y]

    if point_x - 1 >= 0:
        status[point_x - 1][point_y] = not status[point_x - 1][point_y]
    if point_x + 1 <= 4:
        status[point_x + 1][point_y] = not status[point_x + 1][point_y]
    if point_y - 1 >= 0:
        status[point_x][point_y - 1] = not status[point_x][point_y - 1]
    if point_y + 1 <= 5:
        status[point_x][point_y + 1] = not status[point_x][point_y + 1]

    return status


def loop(status):
    actions = [
        [False, False, False, False, False, False],
        [False, False, False, False, False, False],
        [False, False, False, False, False, False],
        [False, False, False, False, False, False],
        [False, False, False, False, False, False]
    ]

    a = 0
    for n in range(0, 2**6):
        s = '0' * (8 - len(bin(a))) + str(bin(a))[2::]
        actions[0] = [bool(int(i)) for i in s]

        for key, n in enumerate(actions[0]):
            if n:
                status = changeStatus(status, 0, key)

        result_actions = take_action(status, actions, 0)
        if result_actions:
            return result_actions
        a += 1

    return None


b = loop(a)
print(b)
