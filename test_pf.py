from unittest import TestCase
from datetime import datetime
from pf import date_to_string, string_to_date


class TestPf(TestCase):
    def test_dates(self):
        now = datetime.now()
        round_trip = string_to_date(date_to_string(now))
        self.assertEqual(now, round_trip)
