

class Queue:

    def __init__(self):
        self.__queue = []

    @property
    def queue(self):
        return self.__queue
    
    
    
    def add(self, name):
        self.__queue.append(name)

    def next(self):
        name = self.__queue[0]
        self.__queue.pop(0)
        return name
    
    def is_empty(self):
        if len(self.__queue) > 0:
            return False
        else:
            return True


queue1 = Queue()

queue1.add("Stephanie")
queue1.add("jan")
queue1.add("Koala")

print(queue1.next())
print(queue1.is_empty())
print(queue1.next())
print(queue1.next())
print(queue1.is_empty())
