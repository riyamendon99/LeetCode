class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        #Not all test cases passed. getting confused. Not able to implement how to decrement left when condition is not met.
        
        #Basic Rule: Increment right. If condition is not met then decrement left and perform decrement calculation until the condition is met. Then increment right.
        left = 0
        right = 0
        # No need to write if else condition to add the key and incremenr if already present. VVVVIMP
        dict1 = collections.defaultdict(int)
        result = 0
        count = 0
        while right<len(fruits):
            dict1[fruits[right]] = dict1[fruits[right]] + 1
            count = count + 1
            
            while len(dict1)>2:
                val = fruits[left]
                dict1[val] = dict1[val] -1
                left = left + 1
                count = count -1
                
                if not dict1[val]:
                    dict1.pop(val)
            result = max(result, count)
            right = right +1
        return result
            
        
        """left = 0
        right = 0
        dictionary = {}
        maxFruits = 0
        while(right<len(fruits)):
            print("Left is", left)
            print("Right is", right)
            if fruits[right] not in dictionary:
                if len(dictionary)==2:
                    val = fruits[left]
                    while(fruits[left] ==val):
                        left = left + 1
                    val = dictionary.pop(val)
                    dictionary[fruits[right]] = 1
                    ptr = left
                    while(fruits[ptr] == fruits[right]):
                        dictionary[fruits[ptr]] = dictionary[fruits[ptr]] + 1
                        ptr = ptr + 1
                else:
                    dictionary[fruits[right]] = 1
            else:
                dictionary[fruits[right]] = dictionary[fruits[right]] + 1
                print("DIctionary is ", dictionary)
            maxFruits = max(maxFruits, sum(dictionary.values()))
            print("Max is ", maxFruits)
            right = right + 1
        return maxFruits"""
        