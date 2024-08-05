class Jar:
    def __init__(self, capacity=12):
            self.capacity = capacity
            self.cookies = 0


    def __str__(self):
        s = ""
        for i in range(self.cookies):
            s += "🍪"
        return s

    def deposit(self, n):
        if self.cookies + n > self._capacity:
            raise ValueError
        else:
            self.cookies += n

    def withdraw(self, n):
        if n > self._capacity:
            raise ValueError
        if self.cookies - n > self.cookies:
            raise ValueError
        else:
            self.cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1:
            raise ValueError
        self._capacity = capacity

