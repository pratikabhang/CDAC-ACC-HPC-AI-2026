class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < 0:
            raise StopIteration

        current = self.start
        self.start -= 1

        return current


countdown = Countdown(5)

for number in countdown:
    print(number)