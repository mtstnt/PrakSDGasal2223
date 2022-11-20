import queue as q

class UndirectedWeightedGraph:
  def __init__(self) -> None:
    self.adj_list = {}

  def add_vertex(self, *vertices: str) -> None:
    for v in vertices:
      self.adj_list[v] = []

  # Graphnya ada weight dan kita mau represent di adjacency list.
  # Jadi kita bisa buat tuple utk setiap edge yg isinya: (vertex_destination, weight)
  def add_edge(self, v1: str, v2: str, weight: int) -> None:
    self.adj_list[v1].append((v2, weight))
    self.adj_list[v2].append((v1, weight))

  def print_list(self) -> None:
    for vertex, edges in self.adj_list.items():
      print(f"{vertex}: ", end="")
      for edge in edges:
        print(f"({edge[0]}, weight: {edge[1]}) ", end="")
      print()

  def print_bfs(self, start: str) -> None:
    # Queue yang menyimpan semua item untuk divisit:
    queue = q.SimpleQueue()
    # Visited list/dict, menyimpan semua vertex yang sudah divisit.
    #   disini pakai dictionary supaya lookupnya cepat. Bisa pakai list juga kalau mau.
    visited = {}
    # Masukkan starting vertex di queue
    queue.put(start)
    while not queue.empty():
      # Ambil vertex dari queue.
      to_visit = queue.get()
      to_visit_edges =  self.adj_list[to_visit]
      # Kalau sudah divisit, ga usah divisit lagi
      if to_visit in visited:
        continue
      print(to_visit, end=" ")
      # Simpen bhw node to_visit sudah divisit.
      visited[to_visit] = True
      # Masukkan element yang ada di edge vertex yang kita visit ke queue.
      for edge in to_visit_edges:
        queue.put(edge[0])
    print()

  def __dfs(self, current: str, visited: dict) -> None:
    # Kalau blm divisit, kita visit dan visit edgenya, else kita skip ga ngapa-ngapain.
    if current not in visited:
      visited[current] = True
      print(current, end=" ")
      for edge in self.adj_list[current]:
        self.__dfs(edge[0], visited)

  def print_dfs(self, start: str) -> None:
    # Panggil fungsi __dfs secara rekursif.
    self.__dfs(start, {})

g = UndirectedWeightedGraph()
g.add_vertex("A", "B", "C", "D")
g.add_edge("A", "B", 5)
g.add_edge("A", "C", 9)
g.add_edge("B", "D", 4)
g.add_edge("C", "B", 8)

print("Adj list: ")
g.print_list()

print("BFS:")
g.print_bfs("B")

print("DFS:")
g.print_dfs("B")