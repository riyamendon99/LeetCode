class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        n = len(gain)
        result = [0]*(n+1)
        for i in range(n):
            x = gain[i] + altitude
            result[i+1] = x
            altitude = x
        return max(result)

        """x-(-5) = 1
        x + 5 = 1
        x = 1-5 = -4"""