#!/usr/bin/env python3
import unittest
from blackbox.broker import Oanda


class TestOanda(unittest.TestCase):

    def setUp(self):
        self.broker = Oanda()
        super().setUp()

    def test_open_order(self):
        self.assertEqual(self.broker.open_order('SHORT', 1, 'EUR_USD'), 201)
        self.assertEqual(self.broker.open_order('LONG', 1, 'EUR_USD'), 201)

    def tearDown(self):
        self.broker.close()


if __name__ == '__main__':
    unittest.main()
