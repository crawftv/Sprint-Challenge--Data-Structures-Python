class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = capacity
    self.storage = [None]*capacity

  def append(self, item):
    index = self.current % self.capacity
    self.storage[index] = item
    self.current +=1

  def get(self):
    return [ i for i in self.storage if i is not None]
