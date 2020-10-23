# Last In First Out LIFO
# array -> list 模拟


class Stack:
    length = 0
    store = []

    def __init__(self, *args):
        self.store = list(args)
        self.length = len(self.store)

    def pop(self):
        self.length -= 1
        top_element = self.store[self.length]
        del self.store[self.length]
        return top_element

    def push(self, value):
        self.store.append(value)  # not static store, only can append
        self.length += 1

    def __len__(self):
        return len(self.store)


# test
s = Stack('a', 'b', 'c')
print(s.pop())
s.push('ccc')
s.push('ddd')
print(len(s))
print(s.pop())
print(s.pop())
print(s.pop())

# 链式存储的栈

# TODO(rust) 用栈实现四则运算， 包括将中缀表达式转化为后缀表达式（逆波兰表达式）， 或者是前缀表达式（lisp）
