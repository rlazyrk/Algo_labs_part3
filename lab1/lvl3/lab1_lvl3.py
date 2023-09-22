import unittest

def find_unsorted_part(nums):
    n = len(nums)
    left = 0
    right = n - 1
    while left < n - 1 and nums[left] <= nums[left + 1]:
        left += 1
    if left == n - 1:
        return (-1, -1)
    while right > 0 and nums[right] >= nums[right - 1]:
        right -= 1
    min = nums[left]
    max = nums[right]
    for i in range(left, right+1):
        if min > nums[i]:
            min = nums[i]
        if max < nums[i]:
            max = nums[i]
    while left > 0 and nums[left-1] > min:
        left -= 1
    while right < n - 1 and nums[right+1] < max:
        right += 1
    return (left, right)
    
class Tests(unittest.TestCase):
    def test_sorted_arr(self):
        test_list = [1,2,3,4,5,6,7,8,9]
        left,right = find_unsorted_part(test_list)
        self.assertEqual(left, -1)
        self.assertEqual(right, -1)
    
    def test_reverse_sorted_arr(self):
        test_list = [9,8,7,6,5,4,3,2,1]
        left,right = find_unsorted_part(test_list)
        self.assertEqual(left, 0)
        self.assertEqual(right,8)
        
    def test_partly_unsorted_arr(self):
        test_list = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
        left,right = find_unsorted_part(test_list)
        self.assertEqual(left, 3)
        self.assertEqual(right,9)
    
    def test_full_same_list(self):
        test_list = [7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7]
        left,right = find_unsorted_part(test_list)
        self.assertEqual(left, -1)
        self.assertEqual(right, -1)
        
unittest.main()

    
