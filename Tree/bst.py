
# Binary Search Tree -> 2 node, left dan right.
class Node:
  value: int
  left: "Node"
  right: "Node"

  def __init__(self, value: int) -> None:
    self.value = value
    self.left = self.right = None

class BST:
  root: Node

  def __init__(self) -> None:
    self.root = None

  # Bonus: *values -> variadic argument, biar masukin insert(1, 2, 3, 4, 5) -> berarti insert angka" tersebut dlm 1 panggilan fungsi.
  def insert(self, *values: int) -> None:
    for value in values:
      # First insert masuk ke root.
      if self.root is None:
        self.root = Node(value)
        continue
      
      # Kalau lebih kecil dari parent, maka masuk ke kiri, else masuk kanan. 
      current = self.root
      while True:
        if value <= current.value:
          if current.left is None:
            current.left = Node(value)
            break
          else:
            current = current.left
        else:
          if current.right is None:
            current.right = Node(value)
            break
          else:
            current = current.right

  # Search using BST characteristics.
  def __exists_bst_dfs(self, node: Node, searched: int) -> bool:
    if node is None:
      return False
    if node.value == searched:
      return True

    if searched <= node.value:
      return self.__exists_bst_dfs(node.left, searched)
    else:
      return self.__exists_bst_dfs(node.right, searched)

  def exists_bst(self, value: int) -> bool:
    return self.__exists_bst_dfs(self.root, value)

  def __dfs(self, node: Node, indent = 0) -> None:
    if node is None:
      return
    for _ in range(indent): print(" ", end="")
    print(node.value)
    self.__dfs(node.left, indent + 1)
    self.__dfs(node.right, indent + 1)

  # Search all in tree.
  def __search_all(self, node: Node, searched: int) -> bool:
    if node is None:
      return False
    if node.value == searched:
      return True
    return self.__search_all(node.left, searched) or self.__search_all(node.right, searched)

  def search_all(self, value: int) -> bool:
    return self.__search_all(self.root, value)

  def view(self) -> None:
    self.__dfs(self.root)

def main() -> None:
  bst = BST()
  bst.insert(2, 1, 2, 3, 5, 9)
  bst.view()

  print("Searching for 4: ", bst.exists_bst(4))
  print("Searching for 9: ", bst.exists_bst(9))

# Entrypoint-nya Python.
if __name__ == "__main__":
  main()