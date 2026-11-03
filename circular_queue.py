class Circular:
    def __init__(self, size):
        self.queue = [None] * size
        self.max_size = size
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.max_size == self.front:
            print("Queue is full")

        elif self.front == -1:
            self.rear = 0
            self.front = 0
            self.queue[self.rear] = item

        else:
            self.rear = (self.rear + 1) % self.max_size
            self.queue[self.rear] = item

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")

        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp

        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.max_size
            return temp

    def is_empty(self):
        return self.front == -1

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.front]


circular = Circular(5)

circular.enqueue(1)

print(circular.peek())
print(circular.dequeue())
print(circular.is_empty())
