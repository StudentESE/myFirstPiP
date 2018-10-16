import unittest
import myModule
class TestMyMethod(unittest.TestCase):
    def test_myMethod(self):
        self.assertEqual(myModule.myMethod(), "Hello PiP")
if __name__ == '__main__':
    unittest.main()