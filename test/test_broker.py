#!/usr/bin/env python3
import unittest
from modules.broker import Oanda


class TestBroker(unittest.TestCase):

    def test_summary(self):
        self.assertResponse(
            summary()['currency'], 'EUR', 'Should be EUR.')
