# Implementing class using python class


class Stack:
    def __init__(self):
        self.items = []

    def empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def show(self):
        print(self.items)


s = Stack()
a = []
print(s.empty())
s.push(5)
s.push(8)
val = s.pop()
a.append(val)
s.push(2)
s.push(5)
val = s.pop()
a.append(val)
val = s.pop()
a.append(val)
val = s.pop()
a.append(val)
s.push(1)
val = s.pop()
a.append(val)
print(a)
