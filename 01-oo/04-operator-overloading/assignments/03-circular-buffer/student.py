

class CircularBuffer:

    def __init__(self, lenght):
        self.buffer = []
        self.lenght = lenght

    


    def add(self, item):
        if len(self.buffer) == self.lenght:
            self.buffer.pop(0)
            self.buffer.append(item)
        if len(self.buffer) <self.lenght:
            self.buffer.append(item)

    def __len__(self):
        return len(self.buffer)
    
    def __getitem__(self, item):
        return self.buffer[item]
    
# buffer = CircullarBuffer(3)

# print(len(buffer))

# buffer.add("a")
# buffer.add("b")
# buffer.add("c")
# buffer.add("d")
# buffer.add("e")

# print(len(buffer))