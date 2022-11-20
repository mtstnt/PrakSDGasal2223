class Node:
  def __init__(self, value: any) -> None:
    self.value = value
    self.next = None

  def __repr__(self) -> str:
    return f"({self.value} {self.next})"

class LischHashTable:
  def __init__(self, capacity: int = 100) -> None:
    self.table: list[Node] = [None] * capacity
    self.capacity = capacity

  def __hash_fn(self, item: any) -> int:
    return item % self.capacity

  def insert(self, item: any) -> None:
    idx = self.__hash_fn(item)
    # Kalau kosong langsung diletakkan
    if self.table[idx] is None:
      self.table[idx] = Node(item)

    # Kalau sudah ada isinya,
    # Ke link paling akhir, lalu disambungkan dgn node yang baru
    else:
      iterator = self.table[idx]
      while iterator.next is not None:
        iterator = self.table[iterator.next]
      for i in range(self.capacity - 1, -1, -1):
        if self.table[i] is None:
          self.table[i] = Node(item)
          iterator.next = i
          break

  def search(self, item: any) -> tuple[bool, int, int]:
    idx = self.__hash_fn(item)
    iterator = self.table[idx]

    # Iterate dari awal idx ditemukan sampai akhir link.
    prev, current_idx = -1, idx
    if iterator.value == item:
      return True, prev, current_idx

    while iterator.next is not None:
      prev = current_idx
      current_idx = iterator.next
      iterator = self.table[current_idx]

      if iterator.value == item:
        return True, prev, current_idx

    return False

  def delete(self, item: any) -> None:
    is_found, previous_key, index = self.search(item)
    if not is_found:
      raise Exception(f"key {item} not found in hash table")
    
    # First hit
    if previous_key == -1:
      iterator = self.table[index]
      prev, current = -1, index

      # Timpa value dengan value di link selanjutnya.
      while iterator.next is not None:
        iterator.value = self.table[iterator.next].value
        prev = current
        current = iterator.next
        iterator = self.table[iterator.next]
        
      # Hapus link selanjutnya dari link terakhir.
      # Hapus element yang di akhir link.
      self.table[prev].next = None
      self.table[current] = None

    # Hit is in a link
    else:
      # Set nextnya previous link ke nextnya dari link yang didelete ini. (Spt delete di linked list)
      self.table[previous_key].next = self.table[index].next
      # Set current as None
      self.table[index] = None

  def print(self) -> None:
    for i in range(len(self.table)):
      print(f"{i} {self.table[i]}")