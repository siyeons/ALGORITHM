def canMeasureWater(x: int, y: int, z: int) -> bool:
    print(gcd(x,y))
    if gcd(x, y) == 0 and x + y == z:
        return True
    if gcd(x, y) == 0 and x + y != z:
        return False
    if gcd(x, y) == 1:
        return True
    if z != 0 and z % gcd(x, y) == 0:
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

print(canMeasureWater(0, 0, 1))