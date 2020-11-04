import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):#must inherit from unittest.TestCase (so Py knows how to run test)

    def test_first_last_name(self):# Any method that starts with test_ will be run automatically when we run test_name_function.py
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')#Assert methods verify that a result you received matches the result you expected to receive

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__': # many testing frameworks import test files before running them.  When a file is imported, the interpreter executes the file as it’s being imported
    # variable  __name__ is set when the ptogramm is executed. If this file is being run as the main program, the value of name is set to __main__we call unittest.main(), which runs the test case
    # When a testing framework imports this file, the value of __name__ won’t be '__main__' and this block will not be executed.
    unittest.main()
