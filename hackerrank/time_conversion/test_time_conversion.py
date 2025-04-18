import unittest

from time_conversion import time_conversion

class TestTimeConversion(unittest.TestCase):

    def test_am_case_1(self):
        """Test a typical AM time (e.g., 07:05:45AM)"""
        self.assertEqual(time_conversion("07:05:45AM"), "07:05:45")

    def test_pm_case_1(self):
        """Test a typical PM time (e.g., 07:05:45PM)"""
        self.assertEqual(time_conversion("07:05:45PM"), "19:05:45")

    def test_midnight_am(self):
        """Test 12:00:00AM (noon in AM) - should be 00:00:00"""
        self.assertEqual(time_conversion("12:00:00AM"), "00:00:00")

    def test_noon_pm(self):
        """Test 12:00:00PM (midnight in PM) - should be 12:00:00"""
        self.assertEqual(time_conversion("12:00:00PM"), "12:00:00")

    def test_afternoon_pm(self):
        """Test a morning time in PM (e.g., 01:01:01PM)"""
        self.assertEqual(time_conversion("01:01:01PM"), "13:01:01")

    def test_early_am(self):
        """Test an evening time in AM (e.g., 05:05:05AM)"""
        self.assertEqual(time_conversion("05:05:05AM"), "05:05:05")

    def test_leading_zero_am(self):
        """Test AM time with leading zero on hour."""
        self.assertEqual(time_conversion("01:01:01AM"),"01:01:01")

    def test_leading_zero_pm(self):
        """Test PM time with leading zero on hour."""
        self.assertEqual(time_conversion("02:02:02PM"),"14:02:02")


if __name__ == '__main__':
    unittest.main()