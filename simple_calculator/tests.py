import unittest
from unittest.mock import patch

from client import Client
from server import CalculatorServer


class ClientTests(unittest.TestCase):

    def setUp(self):
        self.c = Client()

    def tearDown(self):
        self.c.s.close()

    @patch("client.Client.get_input")
    def test_should_input_correct_message(self, mock_input):
        mock_input.return_value = "2+2"
        calculation = self.c.get_input()
        self.assertEqual(calculation, "2+2")

    @patch('client.Client.send_calculation')
    def test_should_send_calculations(self, mock_send):
        data = "3+3"
        self.c.send_calculation(data)
        self.assertTrue(mock_send.call_count, 1)
        mock_send.assert_called_once_with("3+3")


class ServerTests(unittest.TestCase):
    def setUp(self):
        self.serv = CalculatorServer()

    def tearDown(self):
        self.serv.s.close()

    def test_calculate_should_return_sum(self):
        data = "1+1"
        self.assertEqual(self.serv.calculate(data), 2)

    def test_calculate_should_return_subtraction(self):
        data = "5-1"
        self.assertEqual(self.serv.calculate(data), 4)

    def test_calculate_should_return_multiplication(self):
        data = "10*2"
        self.assertEqual(self.serv.calculate(data), 20)

    def test_calculate_should_return_division(self):
        data = "40/4"
        self.assertEqual(self.serv.calculate(data), 10)

    def test_calculate_should_return_message_when_divide_by_0(self):
        data = "5/0"
        self.assertEqual(self.serv.calculate(data), "You can not divide by 0")

    def test_calculate_should_return_message_when_no_calculations(self):
        data = "500"
        self.assertEqual(self.serv.calculate(data), "Can not do calculations")

    def test_server_should_close_when_data_exit(self):
        data = "exit"
        self.assertRaises(SystemExit, self.serv.calculate, data)


if __name__ == "__main__":
    unittest.main()
