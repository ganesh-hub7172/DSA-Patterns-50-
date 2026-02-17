class BrowserHistory(object):

    def __init__(self, homepage):
        self.hist = [homepage]
        self.i = 0

    def visit(self, url):
        self.hist = self.hist[:self.i + 1]
        self.hist.append(url)
        self.i += 1

    def back(self, steps):
        self.i = max(0, self.i - steps)
        return self.hist[self.i]

    def forward(self, steps):
        self.i = min(len(self.hist) - 1, self.i + steps)
        return self.hist[self.i]
