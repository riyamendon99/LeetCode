class LUPrefix:
    """Watched Video"""
    """Logic: An aray full of False values with length n
    and keep one variable maxVal that stores the longest valid prefix
    Only increment it if the values are continuously True"""
    def __init__(self, n: int):
        self.arr = [False]*(n+1)
        self.maxVal = 0

    def upload(self, video: int) -> None:
        self.arr[video-1] = True
        while self.arr[self.maxVal] == True:
            self.maxVal += 1

    def longest(self) -> int:
        return self.maxVal
    
"""My Approach: Brute Force. Getting Time Limit Exception
    def __init__(self, n: int):
        self.arr = []

    def upload(self, video: int) -> None:
        self.arr.append(video)

    def longest(self) -> int:
        for i in range(1,len(self.arr)+1):
            if i not in self.arr:
                return max(0,i-1)
        return len(self.arr)"""
            
        
# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()