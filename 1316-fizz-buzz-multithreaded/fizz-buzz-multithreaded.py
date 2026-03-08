from threading import Lock

class FizzBuzz:
    def __init__(self, n):
        self.n = n
        self.i = 1
        self.lock = Lock()

    def fizz(self, printFizz):
        while True:
            self.lock.acquire()
            if self.i > self.n:
                self.lock.release()
                return
            if self.i % 3 == 0 and self.i % 5 != 0:
                printFizz()
                self.i += 1
            self.lock.release()

    def buzz(self, printBuzz):
        while True:
            self.lock.acquire()
            if self.i > self.n:
                self.lock.release()
                return
            if self.i % 5 == 0 and self.i % 3 != 0:
                printBuzz()
                self.i += 1
            self.lock.release()

    def fizzbuzz(self, printFizzBuzz):
        while True:
            self.lock.acquire()
            if self.i > self.n:
                self.lock.release()
                return
            if self.i % 3 == 0 and self.i % 5 == 0:
                printFizzBuzz()
                self.i += 1
            self.lock.release()

    def number(self, printNumber):
        while True:
            self.lock.acquire()
            if self.i > self.n:
                self.lock.release()
                return
            if self.i % 3 != 0 and self.i % 5 != 0:
                printNumber(self.i)
                self.i += 1
            self.lock.release()