a = [
    [True, True, True, True, True, True],
    [True, True, True, True, True, True],
    [True, True, True, True, True, True],
    [True, True, True, True, True, True],
    [True, True, True, True, True, True]
]


def take_action(prev_status, status, line, actions):
    for i in range(0, 6):
        if prev_status[i]:
            actions[line][i] = True
            status = changeStatus(status, line, i)
        else:
            actions[line][i] = False

    if line == 4:
        for n in status[4]:
            if n:
                return False
        print("after status: ")
        print(status)
        print("actions:")
        return actions
    else:
        return take_action(status[line], status, line + 1, actions)


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
    t = (False, True)
    for a1 in t:
        for a2 in t:
            for a3 in t:
                for a4 in t:
                    for a5 in t:
                        for a6 in t:
                            first_action = [a1, a2, a3, a4, a5, a6]
                            for key, n in enumerate(first_action):
                                if n:
                                    status = changeStatus(status, 0, key)

                            result_actions = take_action(
                                status[0], status, 1, actions)
                            if result_actions:
                                result_actions[0] = first_action
                                return result_actions
    return None


b = loop(a)
print(b)
