class MyCircularDeque:
    def __init__(self, k):
        self.size = k
        self.deque = [0] * k
        self.front = -1  # points to the front element
        self.rear = -1   # points to the rear element

    def insertFront(self, value):
        if self.isFull():
            return False
        if self.isEmpty():  # first element
            self.front = self.rear = 0
        else:
            self.front = (self.front - 1 + self.size) % self.size
        self.deque[self.front] = value
        return True

    def insertLast(self, value):
        if self.isFull():
            return False
        if self.isEmpty():  # first element
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.deque[self.rear] = value
        return True

    def deleteFront(self):
        if self.isEmpty():
            return False
        if self.front == self.rear:  # only one element
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False
        if self.front == self.rear:  # only one element
            self.front = self.rear = -1
        else:
            self.rear = (self.rear - 1 + self.size) % self.size
        return True

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.deque[self.front]

    def getRear(self):
        if self.isEmpty():
            return -1
        return self.deque[self.rear]

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        return (self.rear + 1) % self.size == self.front
