# 模拟连续空间的列表 python's list type is array(array list).
class ArrayList:
    max_size = 0
    stores = {}

    def __init__(self, max_size, *values):
        self.max_size = max_size
        self.stores = {key: value for key, value in enumerate(values)}

    # O(n)
    def get_key(self, value):
        for key, value in self.stores.items():
            if value == value:
                return key

    # O(1)
    def get_value(self, key):
        if key >= 0 and key < self.max_size:
            return self.stores[key]

    def len(self):
        return len(self.stores)

    # O(n)
    def add_element(self, value, set_key=None):
        if set_key == None and self.len() < self.max_size - 1:
            self.stores[self.len()] = value

        elif set_key >= 0 and set_key < self.max_size and self.len() < (self.max_size - 1):
            for i in range(self.len(), set_key, -1):
                self.stores[i] = self.stores[i - 1]

            self.stores[set_key] = value

    # O(n)
    def del_element(self, del_key):
        if del_key >= 0 and del_key < (self.len() - 1):
            for i in range(del_key, self.len() - 1):
                self.stores[i] = self.stores[i + 1]

            del self.stores[self.len() - 1]

    def __repr__(self):
        for key, value in self.stores.items():
            print(key, ': ', value)

        return 'len_size: ' + str(self.len())


# test
array_list = ArrayList(10, 'a', 'b', 'c')
print(array_list.len())
print(array_list.get_key('a'))
print(array_list.get_value(1))

array_list.add_element('d')
print(array_list.len())

array_list.add_element('bbb', 1)
print(array_list)

array_list.del_element(1)
print(array_list)
