import unittest

def findMinSquare(N, W, H):
    if not (1 <= N <= 10**12) or not (1 <= W <= 10**9) or not (1 <= H <= 10**9):
        return (-1, -1)
    i = 1
    j = W * H * N
    while i < j:
        mid = ( i + j ) // 2
        current = (mid // W) * (mid // H)
        if current >= N:
            j = mid
        else:
            i = mid + 1
    return j

class TestFindMinSquare(unittest.TestCase):
    def testOutOfRange(self):
        expected = (-1,-1)
        result = findMinSquare(10**13,1,1)
        result2 = findMinSquare(1,10**10,1)
        result3 = findMinSquare(1, 1, 10**10)
        self.assertEqual(expected, result)
        self.assertEqual(expected, result2)
        self.assertEqual(expected, result3)
    
    def testNormalValue(self):
        expected = 9
        expected2 = 2
        result = findMinSquare (10,2,3)
        result2 = findMinSquare(4,1,1)
        self.assertEqual(expected, result)
        self.assertEqual(expected2, result2)
print(findMinSquare(3,100,111))
unittest.main()

