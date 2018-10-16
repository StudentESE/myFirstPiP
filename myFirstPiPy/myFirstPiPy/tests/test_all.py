import unittest
import __init__ as myModule
class TestMyMethod(unittest.TestCase):
    def test_myMethod(self):
        self.assertEqual(myModule.myMethod(), "Hello PiP")
    def test_myVariable(self):
        self.assertIs(myModule.myVariable, 123)
if __name__ == '__main__':
    unittest.main()