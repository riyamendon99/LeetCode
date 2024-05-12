class Solution:
    
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        
        def getXOR(x, y):
            return (x | y) & (~x | ~y)
        
        heap = []
        hashMap = {}
        value = 0
        for i in range (len(matrix)):
            for j in range(len(matrix[0])):
                value = matrix[i][j]
                if i-1>=0:
                    value = getXOR(matrix[i][j], hashMap[(i-1,j)])
                if j-1>=0:
                    value = getXOR(value, hashMap[(i,j-1)])
                if j-1>=0 and i-1>=0:
                    value = getXOR(value, hashMap[(i-1,j-1)])
                hashMap[(i,j)] = value
                heappush(heap,value)
                
                    
        result = heapq.nlargest(k, heap)
        print(result)
        return result[k-1]
                        
                        
                        
                
                
            
        