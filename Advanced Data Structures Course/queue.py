class Queue:
    def __init__(self):
        self.queue = []

    def add(self, dataval):
        if dataval not in self.queue:
            self.queue.append(dataval)
        else:
            print("Data already in queue")
            return False
    def remove(self):
        if len(self.queue) < 1:
            print("No element in queue")
        else:
            return self.queue.pop(0)
AQueue = Queue()
AQueue.add("Mon")
AQueue.add("Tue")
AQueue.add("Wed")
AQueue.add("Thu")
AQueue.add("Fri")
AQueue.add("Sat")
AQueue.add("Sun")
print(AQueue.remove())
print(AQueue.remove())