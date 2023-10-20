import unittest


def funk(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return i,j
    return -1
                
                
class Tests(unittest.TestCase):
    def test_successfull(self):
        test_list = [1,23,56,1234,6776]
        first_index, second_index = funk(test_list,57)
        self.assertEqual(first_index,0)
        self.assertEqual(second_index,2)

    def test_failed(self):
        test_list = [1,23,56,1234,6776]
        result = funk(test_list,58)
        self.assertEqual(result,-1)


unittest.main()