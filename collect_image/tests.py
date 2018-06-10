import unittest, os
from collect_image.func import download_image

class MyFuncTests(unittest.TestCase):

    def setUp(self):
        self.test_url = "https://2.bp.blogspot.com/-JvZNMcYeJXg/WRDKJQ10xCI/AAAAAAAALAg/9I7cd3n0bbE7V9t8TqsJ1OPqyJDxghycwCPcB/s1600/DSCF2275.JPG"
        self.dirname = os.getcwd()


    def tearDown(self):
        os.remove(self.dirname + "/image.jpg")

    def test_should_download_image(self):
        download_image(self.test_url)
        self.assertTrue(os.path.isfile(self.dirname + "/image.jpg"))