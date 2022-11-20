class LinklessHashTable:
  def __init__(self, capacity: int = 100) -> None:
    self.table = [None] * capacity
    self.capacity = capacity

  def insert(self, item: any) -> None:
    idx = self.__hash_fn(item)
    if self.table[idx] is None:
      self.table[idx] = [item]
    else:
      self.table[idx].append(item)

  def __hash_fn(self, item: any) -> int:
    return item % self.capacity

  def search(self, item: any) -> bool:
    idx = self.__hash_fn(item)
    items = self.table[idx]
    if items is None:
      return False
    for i in items:
      if item == i:
        return True
    return False

  def print(self) -> None:
    for i in self.table:
      print(i)