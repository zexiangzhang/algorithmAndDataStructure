#从a移动到c上, b为中间转
def hanoi(n, a='A', b='B', c='C'):
    print(n)
    if n == 1:
        print('move', a, '-->', c)
        return
    hanoi(n - 1, a, c, b)
    print('move', a, '-->', c)
    hanoi(n - 1, b, a, c)


print('any no number key to stop')
while True:
    try:
        n = abs(int(input('n: ')))
        hanoi(n)
    except ValueError:
        break
