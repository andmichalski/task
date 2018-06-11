import unittest
from unittest.mock import patch

from simple_calculator.client import MyClient


class ClientTests(unittest.TestCase):
    def setUp(self):
        self.c = MyClient()

    def tearDown(self):
        self.c.close()

    @patch("simple_calculator.client.MyClient.get_input")
    def test_should_input_correct_message(self, mock_input):
        mock_input.return_value = "2+2"
        calculation = self.c.get_input()
        self.assertEqual(calculation, "2+2")

        my_socket = self.c.send_equation(calculation)
        print(my_socket)
