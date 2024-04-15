class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = []
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                arr.append(matrix[i][j])
        heapq.heapify(arr)
        l = heapq.nsmallest(k, arr)
        return l[-1]