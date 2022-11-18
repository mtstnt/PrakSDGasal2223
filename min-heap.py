import math

class MinHeap:
    def __init__(self, initial_values: list[int] = []) -> None:
        self.heap = initial_values
        self.__build_min_heap()

    def insert(self, value: int) -> None:
        self.heap.append(value)
        current = len(self.heap) - 1
        while self.heap[current] < self.heap[self.__parent(current)]:
            parent_idx = self.__parent(current)
            self.heap[current], self.heap[parent_idx] = self.heap[parent_idx], self.heap[current]
            current = parent_idx

    def get(self) -> int:
        if len(self.heap) == 0:
            raise IndexError("heap is empty!")
        return self.heap[0]

    def pop(self) -> int:
        if len(self.heap) == 0:
            raise IndexError("heap is empty!")
        minimum = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self.__min_heapify(0)
        return minimum

    def remove(self, value: int) -> None:
        to_delete = self.heap.index(value)
        self.heap.pop(to_delete)
        self.__build_min_heap()
        
    def __len__(self) -> int:
        return len(self.heap)

    def print(self) -> None:
        self.__print(0)

    def __print(self, k: int, level: int = 0, side: int = 0) -> None:
        if k >= len(self.heap):
            return
        for _ in range(level):
            print(end="-")
        side_str = ["ROOT", "L", "R"][side]  # 0: ROOT, 1: L, 2: R
        print(f"{self.heap[k]} ({side_str})")
        self.__print(2 * k + 1, level + 1, 1)
        self.__print(2 * k + 2, level + 1, 2)

    def __build_min_heap(self) -> None:
        # self.heap[N / 2 + 1] s.d self.heap[N - 1] -> leaf nodes
        n = int((len(self.heap) // 2) - 1)
        for k in range(n, -1, -1):
            self.__min_heapify(k) # O(log n)

    def __get_left_child_index(self, k: int) -> int:
        return 2 * k + 1

    def __get_right_child_index(self, k: int) -> int:
        return 2 * k + 2

    def __min_heapify(self, k: int) -> None:
        left = self.__get_left_child_index(k)
        right = self.__get_right_child_index(k)
        smallest = k

        if left < len(self.heap) and self.heap[left] < self.heap[k]:
            smallest = left
            
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != k:
            # Swap k and smallest
            self.heap[k], self.heap[smallest] = self.heap[smallest], self.heap[k]

            # Min heapify lagi ke bawah (cek apakah swap di node atas" ngefek ke urutan di node bawahnya)
            self.__min_heapify(smallest)

    def __parent(self, k: int) -> int:
        if k == 0: return 0
        elif k % 2 == 0: return k // 2 - 1
        else: return k // 2

def main() -> None:
    heap = MinHeap([9])
    heap.print()
    print()

    heap.insert(8)
    heap.insert(6)
    heap.insert(7)
    heap.insert(5)
    heap.insert(2)
    heap.insert(4)
    print()

    heap.insert(2)
    heap.print()
    print()

    heap.remove(5)
    heap.remove(2)
    heap.print()
    print()

if __name__ == "__main__":
    main()
