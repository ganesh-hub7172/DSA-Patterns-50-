class NestedIterator:
    def __init__(self, nestedList):
        # Stack holds elements in reverse order
        self.stack = nestedList[::-1]

    def next(self):
        return self.stack.pop().getInteger()

    def hasNext(self):
        while self.stack:
            top = self.stack[-1]

            if top.isInteger():
                return True
            else:
                # Expand the list
                self.stack.pop()
                for item in reversed(top.getList()):
                    self.stack.append(item)
        return False
