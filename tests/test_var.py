import unittest
import myModule
class TestMyMethod(unittest.TestCase):
    def test_myVariable(self):
        self.assertIs(myModule.myVariable, 123)
if __name__ == '__main__':
    unittest.main()