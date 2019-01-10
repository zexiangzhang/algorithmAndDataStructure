# First In First Out FIFO
# 单队列， 会出现假溢出
# 循环队列


class Queue:
    max_size = 0
    store = []
    top_pointer = 0
    tail_pointer = 0

    def __init__(self, max_size, *args):
        if len(args) < max_size:
            self.max_size = max_size
            self.store = list(args)
            self.store += [None for i in range(len(args), max_size)]
            self.tail_pointer = len(args) - 1
        else:
            self.max_size = max_size

    def pop(self):
        value = self.store[self.top_pointer]
        self.store[self.top_pointer] = None
        self.top_pointer += 1
        if self.top_pointer == self.max_size:
            self.top_pointer = 0

        return value

    def push(self, value):
        if (self.tail_pointer + 1) % self.max_size != self.top_pointer:
            if self.tail_pointer + 1 == self.max_size:
                self.tail_pointer = 0
            else:
                self.tail_pointer += 1

            self.store[self.tail_pointer] = value

    def __repr__(self):
        print(self.store)
        return 'top_pointer: ' + str(self.top_pointer) + ', tail_pointer: ' + str(self.tail_pointer)


# test
d = Queue(5, 'a', 'b')
print(d)
d.push('c')
d.push('d')
d.push('e')
d.push('e')
d.push('e')
d.push('e')
print(d)
d.pop()
d.pop()
d.pop()
print(d)
d.push('1')
d.push('2')
print(d)
d.push('3')
d.push('4')
print(d)

# 链式队列
