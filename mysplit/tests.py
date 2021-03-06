import unittest

from my_split import my_split


class MySplitTests(unittest.TestCase):

    def test_should_return_list_when_separator_double_dots(self):
        base_string = "Make:it:as:simple:as:possible"
        out_list = ["Make", "it", "as", "simple", "as", "possible"]
        self.assertEqual(my_split(base_string, ":"), out_list)

    def test_should_return_empty_list_when_only_separator(self):
        base_string = ":"
        out_list = []
        self.assertEqual(my_split(base_string, ":"), out_list)

    def test_should_return_list_with_input_when_no_separator_in_input(self):
        base_string = "some_string"
        out_list = ["some_string"]
        self.assertEqual(my_split(base_string, ";"), out_list)

    def test_should_return_list_when_separator_semicolon(self):
        base_string = "Simple;test"
        out_list = ["Simple", "test"]
        self.assertEqual(my_split(base_string, ";"), out_list)


if __name__ == "__main__":
    unittest.main()
