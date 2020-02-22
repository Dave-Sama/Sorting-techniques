# radix sort:

import time
start_time = time.time()

class Node:

    def __init__(self, data):
        self.next = None
        self.data = data
class Linked:
    def __init__(self, node):
        self.head = None
        self.tail = None
        self.size = 0
        self.append(node)

    def append(self, node):

        if self.size > 0:
            self.tail.next = node
            self.tail = self.tail.next
            self.tail.next = None
            self.size += 1
        elif self.size == 0:
            self.head = self.tail = node
            self.tail.next = None
            self.size += 1

    def traversal(self):
        b = []
        cur = self.head
        while cur != None:
            b.append(cur.data)
            cur = cur.next

        return b




def new_node(data):
    return Node(data)


def radix(a):
    maxi = max(a)
    count = 0
    while maxi > 0:
        count += 1
        maxi = maxi // 10

    b = [None for _ in range(len(a)+1)]
    c = []
    print(b)

    j = 0
    num = 1
    while j < count:

        for i in a:
                if b[(i//num)%10] == None:
                    b[(i//num)%10] = Linked(new_node(i))
                else:
                    b[(i//num)%10].append(new_node(i))

        c = []
        for i in b:
            if i != None:
                c = c + i.traversal()
        a = c
        b = [None for _ in range(len(a) + 1)]

        j += 1
        num = int(str(num) + '0')
    return a


a = [4, 98, 110, 74, 9, 31, 199, 36, 0]
a = radix(a)

print(a)
print("My program took", round(time.time() - start_time, 3), "to run")
