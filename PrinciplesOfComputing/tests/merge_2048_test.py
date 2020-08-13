import unittest
from .. import merge_2048


class Test4048Merge(unittest.TestCase):
    def test_arranging(self):
        self.assertEqual([2, 0], merge_2048.arrange([0, 2]))
        self.assertEqual([2, 0, 0], merge_2048.arrange([0, 2, 0]))
        self.assertEqual([2, 4, 0], merge_2048.arrange([0, 2, 4]))
        self.assertEqual([2, 2, 0], merge_2048.arrange([0, 2, 2]))
        self.assertEqual([2, 4, 0, 0], merge_2048.arrange([0, 2, 0, 4]))
        self.assertEqual([2, 2, 0, 0], merge_2048.arrange([0, 2, 0, 2]))
        self.assertEqual([4, 0, 0, 0], merge_2048.arrange([0, 0, 0, 4]))
        self.assertEqual([2, 8, 4, 0], merge_2048.arrange([0, 2, 8, 4]))

    def test_merge_equal(self):
        self.assertEqual([2, 0, 0], merge_2048.merge_equal([2, 0, 0]))
        self.assertEqual([2, 4, 0], merge_2048.merge_equal([2, 4, 0]))
        self.assertEqual([4, 0], merge_2048.merge_equal([2, 2, 0]))
        self.assertEqual([4, 0, 0], merge_2048.merge_equal([2, 2, 0, 0]))
        self.assertEqual([16, 2, 0], merge_2048.merge_equal([8, 8, 2, 0]))
        self.assertEqual([4, 0, 0, 0], merge_2048.merge_equal([4, 0, 0, 0]))
        self.assertEqual([2, 8, 4, 0], merge_2048.merge_equal([2, 8, 4, 0]))
        self.assertEqual([2, 8, 2, 0], merge_2048.merge_equal([2, 8, 2, 0]))
        self.assertEqual([2, 4, 0, 0], merge_2048.merge_equal([2, 4, 0, 0]))

    def test_add_trailing_zeros(self):
        self.assertEqual([2, 0, 0, 0], merge_2048.add_trailing_zeros([2, 0, 0], 4))
        self.assertEqual([2, 4, 0, 0], merge_2048.add_trailing_zeros([2, 4, 0], 4))
        self.assertEqual([4, 0, 0, 0], merge_2048.add_trailing_zeros([4, 0], 4))
        self.assertEqual([4, 0, 0, 0], merge_2048.add_trailing_zeros([4, 0, 0], 4))
        self.assertEqual([8, 2, 0, 0], merge_2048.add_trailing_zeros([8, 2, 0], 4))

    def test_merge(self):
        self.assertEqual([2, 0, 0, 0], merge_2048.merge([0, 2, 0, 0]))
        self.assertEqual([2, 0, 0, 0], merge_2048.merge([0, 2, 0, 0]))
        self.assertEqual([2, 4, 0, 0], merge_2048.merge([0, 2, 4, 0]))
        self.assertEqual([4, 0, 0, 0], merge_2048.merge([0, 2, 2, 0]))
        self.assertEqual([2, 4, 0, 0], merge_2048.merge([0, 2, 0, 4]))
        self.assertEqual([4, 0, 0, 0], merge_2048.merge([0, 0, 0, 4]))
        self.assertEqual([2, 8, 4, 0], merge_2048.merge([0, 2, 8, 4]))
        self.assertEqual([4, 0, 0, 0], merge_2048.merge([0, 2, 0, 2]))
