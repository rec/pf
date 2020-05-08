from unittest import TestCase
from datetime import datetime

import pf


class TestPf(TestCase):
    def test_dates(self):
        now = datetime.now()
        now2 = pf.string_to_date(pf.date_to_string(now))
        self.assertEqual(now, now2)

        dt = datetime(2020, 5, 9, 15, 13, 28, 12345)
        self.assertEqual(pf.date_to_string(dt), '2020-05-08 15:13:28.12345')

        s = '2020/02/02 03:03:03.00000'
        s2 = pf.date_to_string(pf.string_to_date(s))
        self.assertEqual(s, s2)

    def test_dollars(self):
        for s in '10.00', '-123.05':
            cents = pf.string_to_cents(s)
            s2 = pf.cents_to_string(cents)
            self.assertEqual(s, s2)

        self.assertEqual(pf.string_to_cents('10'), 1000)
        self.assertEqual(pf.cents_to_string(1000), '10.00')

        for s in '', '.', '0.', '.0', '0.1', '0.-1', '0.1-', '0.123', '0x100':
            with self.assertRaises(ValueError):
                pf.string_to_cents(s)
