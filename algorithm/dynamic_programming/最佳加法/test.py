# 有个由1-9组成的数字窜中， 将m个+号插入其中， 形成一个表达式。
# 求出表达式最小的值

num = '41234543113534513451424242342345249761522346'
m = 50

if m >= len(num):
    print('min is: {}'.format(sum(map(lambda x: int(x), num))))
