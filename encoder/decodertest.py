import unittest
from decoder import Decoder


class DecoderTest(unittest.TestCase):

    def setUp(self) -> None:
        self.decoder = Decoder()

    def test_encode_if_one_right_symbol(self):
        self.assertEqual('c', self.decoder._Decoder__encode('3'))

    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()

