# -*- coding: utf-8 -*-
import unittest
import DateParser as parser
from datetime import datetime as dt


class DateParserTests(unittest.TestCase):

    def test_single_match(self):
        self.assertEqual(
            [dt(2001, 9, 11)],
            parser.parseDates('2001-09-11')
        )

    def test_double_match(self):
        self.assertEqual(
            [dt(2001, 9, 11), dt(2003, 5, 3)],
            parser.parseDates('2001-09-11 and 2003-5-03')
        )

if __name__ == '__main__':
    unittest.main()
