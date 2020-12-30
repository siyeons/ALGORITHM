class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if z == 0 or (x + y >= z and z % gcd(x, y) == 0):
            return True
        else: 
            return False
    
    def gcd(x, y):
        if (x > y and y == 0):
            return x
        elif (x < y and x == 0):
            return y
        else: 
            while(y):
                x, y = y, x%y
            return x