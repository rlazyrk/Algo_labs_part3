import unittest

def funk(nums):
    result = False
    for i in range(len(nums)-1):
        if nums[i] <= nums[i+1]:
            result = True
        if nums[i] > nums[i+1]:
                result = False
                break
    if result is False:
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                result = True
            if nums[i] < nums[i+1]:
                result = False
                break
    return result       

class Tests(unittest.TestCase):
    def test_successfull_increase(self):
        test_list = [1,5,8,10,25,30,44,100]
        self.assertEqual(funk(test_list),True)
    
    def test_successfull_decrease(self):
        test_list = [100,44,30,25,10,8,5,1]
        self.assertEqual(funk(test_list),True)
    
    def test_failed(self):
        test_list = [100,200,30,44,25,10,35]
        self.assertEqual(funk(test_list),False)
        
        
unittest.main()