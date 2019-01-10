for x in range(0, 100):
    for y in range(0, 100):
        if (100 - x - y) % 3 == 0 and 5 * x + y * 3 + (100 - x - y) / 3 == 100:
            print("鸡翁: {} , 鸡母: {} , 鸡雏: {} ".format(x, y, 100 - x - y))
