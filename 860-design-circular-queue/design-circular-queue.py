class MyCircularQueue:
    def __init__(self, k):
        self.size = k
        self.queue = [0] * k  # fixed-size array
        self.front = -1       # points to the front element
        self.rear = -1        # points to the last element

    def enQueue(self, value):
        if self.isFull():
            return False
        if self.isEmpty():  # first element being inserted
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        if self.front == self.rear:  # only one element
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return True

    def Front(self):
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self):
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        return (self.rear + 1) % self.size == self.front
