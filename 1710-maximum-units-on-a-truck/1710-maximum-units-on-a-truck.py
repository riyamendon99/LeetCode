class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x:x[1], reverse=True)
        print(boxTypes)
        numOfBoxes = 0
        unitSize = 0
        for i in range(len(boxTypes)):
            box = boxTypes[i][0]
            unit = boxTypes[i][1]
            while box:
                if numOfBoxes < truckSize:
                    numOfBoxes += 1
                    unitSize += unit
                    box-=1
                else:
                    return unitSize
        return unitSize
                    
                
        
        