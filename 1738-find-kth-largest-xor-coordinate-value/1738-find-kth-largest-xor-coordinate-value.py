class Solution:
    
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        """Took 2 hours"""
        #Ratta this formula
        def getXOR(x, y):
            return (x | y) & (~x | ~y)
        """For this type of question where they have asked the below:

The value of coordinate (a, b) of the matrix is the XOR of all matrix[i][j] where 0 <= i <= a < m and 0 <= j <= b < n (0-indexed).


brute force will make it super complex and lead to time limit exception. Use hashMap to store repetitive. ALSO VVVIMP to know which values are being repeated. Take the basic calculation and try to come up with how you can reduce the complexity by reusing values and not calculating them every time.

I first thought that the matrix values need to be stored. But later by trial and error found out that the XOR values need to be stored."""
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
        return result[k-1]
                        
                        
                        
                
                
            
        