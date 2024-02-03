import unittest
import numpy as np

from source_coding.source_coder import source_coder

class source_coding_test(unittest.TestCase):
    def test_ASCIICoder(self):
        coder = source_coder("ASCII")
        array1 = coder.source_code("h")
        array2 = np.array([0,1,1,0,1,0,0,0])
        self.assertTrue(np.array_equal(array1,array2))

if __name__ == "__main__":
    unittest.main()

