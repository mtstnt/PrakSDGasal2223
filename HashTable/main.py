from eisch import EischHashTable
from linkless import LinklessHashTable
from lisch import LischHashTable

def main() -> None:
  # hash1 = LinklessHashTable(10)
  # hash1.insert(99)
  # hash1.insert(199)

  # print(hash1.search(99))
  # print(hash1.search(199))

  hash2 = EischHashTable(10)
  hash2.insert(99)
  hash2.insert(199)
  hash2.insert(299)
  hash2.insert(399)
  hash2.insert(499)
  hash2.insert(599)

  hash2.print()

  print(hash2.search(199))
  print(hash2.search(109))

  hash2.delete(99)
  hash2.delete(599)
  hash2.delete(499)
  print(hash2.search(299))
  hash2.print()

  print()
  print()
  print()
  print()

  hash3 = LischHashTable(10)
  hash3.insert(99)
  hash3.insert(199)
  hash3.insert(299)
  hash3.insert(399)
  hash3.insert(499)
  hash3.insert(599)

  hash3.print()

  print(hash3.search(199))
  print(hash3.search(109))

  hash3.delete(99)
  hash3.delete(599)
  hash3.delete(499)
  print(hash3.search(299))
  hash3.print()

if __name__ == "__main__":
  main()