import unittest
import main

class TestMain(unittest.TestCase):
    def setUp(self):
        print('About to run a function')
    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 20)

    def test_do_stuff2(self):
        test_param = "dasdasda"
        result = main.do_stuff(test_param)
        self.assertTrue(isinstance(result, ValueError))
        # self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please enter a number')

    def test_do_stuff4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def tearDown(self):
        print('clenaning up')

if __name__ == "__main__":

    unittest.main()