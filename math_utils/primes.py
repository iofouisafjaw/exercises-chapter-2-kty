import math
def isprime(n):
    """判断一个数是否为素数"""
    if n <= 1:
        return False
    if n == 2:
        return True  
    if n % 2 == 0:
        return False  
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True