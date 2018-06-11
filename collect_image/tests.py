import os
import unittest
from unittest.mock import patch

import numpy as np
from func import get_image, show_images
from main import collect_image


class MyFuncTests(unittest.TestCase):

    def setUp(self):
        self.test_url = "https://2.bp.blogspot.com/-JvZNMcYeJXg/WRDKJQ10xCI/AAAAAAAALAg/9I7cd3n0bbE7V9t8TqsJ1OPqyJDxghycwCPcB/s1600/DSCF2275.JPG"
        self.dirname = os.getcwd()
        self.data = np.load('test_file.npy')

    def tearDown(self):
        if os.path.isfile(self.dirname + "/bin_image.jpg"):
            os.remove(self.dirname + "/bin_image.jpg")

    @patch('func.get_image')
    def test_should_get_image(self, mock_get_image):
        mock_get_image.return_value = self.data
        file = get_image(self.test_url)
        self.assertIsInstance(file, np.ndarray)

    @patch('func.get_image')
    @patch('func.cv.waitKey')
    def test_should_show_image_and_save_bin_when_ask(self, mock_key, mock_get_image):
        mock_get_image.return_value = self.data
        mock_key.return_value = 115
        show_images(self.data)
        self.assertEqual(mock_key.call_count, 1)
        self.assertTrue(os.path.isfile(self.dirname + "/bin_image.jpg"))

    @patch('func.get_image')
    @patch('func.cv.waitKey')
    def test_should_show_image_and_not_save_bin_after_asking(self, mock_key, mock_get_image):
        mock_get_image.return_value = self.data
        mock_key.return_value = 111
        show_images(self.data)
        self.assertEqual(mock_key.call_count, 1)
        self.assertFalse(os.path.isfile(self.dirname + "/bin_image.jpg"))

    @patch('func.get_image')
    @patch('func.cv.waitKey')
    def test_should_main_function_save_binary_file(self, mock_key, mock_get_image):
        mock_get_image.return_value = self.data
        mock_key.return_value = 115
        collect_image(self.test_url)
        self.assertEqual(mock_key.call_count, 1)
        self.assertTrue(os.path.isfile(self.dirname + "/bin_image.jpg"))

    @patch('func.get_image')
    @patch('func.cv.waitKey')
    def test_should_main_function_not_save_binary_file(self, mock_key, mock_get_image):
        mock_get_image.return_value = self.data
        mock_key.return_value = 111
        collect_image(self.test_url)
        self.assertEqual(mock_key.call_count, 1)
        self.assertFalse(os.path.isfile(self.dirname + "/bin_image.jpg"))


if __name__ == "__main__":
    unittest.main()
