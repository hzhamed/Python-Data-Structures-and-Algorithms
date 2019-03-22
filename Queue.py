class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


17	q=Queue()
18	
19	q.enqueue(4)
20	q.enqueue('dog')
21	q.enqueue(True)
22	print(q.size())