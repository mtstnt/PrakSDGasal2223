import queue as q

# Pake node lagi di tree (Yeeee!)
class Node:
  def __init__(self, value: any) -> None:
    self.value = value
    # Tree bisa berbagai macam. 
    #  - Binary -> dua cabang, left right
    #  - N-ary -> cabang sebanyak n, berarti bisa disimpan di list misalnya
    # Contoh disini binary
    self.left = self.right = None

# Langkahnya: print kiri dan kanan. Kalau sudah null, ga usah ngapa-ngapain.
def __dfs(cur: Node, level) -> None:
  if cur == None: return

  # Ini hanya untuk print spasi tergantung kedalaman.
  for _ in range(level):
    print("  ", end="")

  print(cur.value)

  # Panggil __dfs secara rekursif ke child kiri dan kanan
  __dfs(cur.left, level + 1)
  __dfs(cur.right, level + 1)

def print_dfs(root: Node) -> None:
  # Kita start dari root dan levelnya set 0
  __dfs(root, 0)
  print()

def print_bfs(root: Node) -> None:
  # Buat queue untuk simpan node mana yang akan divisit. Masukkan root/node pertama ke dalamnya.
  queue = q.SimpleQueue()
  queue.put(root)

  while not queue.empty():
    # Ambil node yang akan divisit.
    current = queue.get()
    print(current.value, end=" ")
    if current.left is not None:
      queue.put(current.left)
    if current.right is not None:
      queue.put(current.right)
  print()

# Tree general (tanpa sifat tertentu pas nambah atau ngehapus) umumnya dibuat tanpa class.
# Kalau kita ada sifat tertentu, misal binary search tree, heap, btree, dst. Kita bisa buat dlm class
#  karena sifat nambah, ambil, dll ada logicnya.
root = Node(10)
root.left = Node(20)
root.left.left = Node(30)
root.left.right = Node(40)
root.right = Node(50)
root.right.left = Node(60)

print("DFS: ")
print_dfs(root)

print("BFS: ", end="")
print_bfs(root)
