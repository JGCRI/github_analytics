import unittest

import githubstats.utils as u


class TestUtils(unittest.TestCase):
    """Test `utils.py` functions."""

    def test_leading_zero(self):
        """Tests for leading_zero function."""

        # check for string length greater than 2
        with self.assertRaises(ValueError):
            v = u.leading_zero('000')

        # check for string length less than 1
        with self.assertRaises(ValueError):
            v = u.leading_zero('')

        # ensure zero leads on length 1 string
        self.assertEqual(u.leading_zero('1'), '01')

        # ensure no zero insertion on length 2 string
        self.assertEqual(u.leading_zero('11'), '11')

    def test_convert_google_time(self):
        """Tests for convert_google_time function."""

        expected_input = '2016-10-21T00:00:00Z'
        expected_output = '2016-10-21 00:00:00'

        out_time = u.convert_google_time(expected_input)

        # ensure converted time is as expected
        self.assertEqual(out_time, expected_output)

    def test_get_download_datetime(self):
        """Tests for get_download_datetime function."""

        dt = u.get_download_datetime().split(' ')
        dte = dt[0].split('-')
        tm = dt[1].split(':')

        # check year length
        self.assertEqual(len(dte[0]), 4)

        int_yr = int(dte[0])

        # check year range
        self.assertLessEqual(int_yr, 2999)
        self.assertGreaterEqual(int_yr, 2020)

        # check month length
        self.assertEqual(len(dte[1]), 2)

        int_mth = int(dte[1])

        # check month range
        self.assertLessEqual(int_mth, 12)
        self.assertGreaterEqual(int_mth, 1)

        # check day length
        self.assertEqual(len(dte[2]), 2)

        int_dy = int(dte[2])

        # check day range
        self.assertLessEqual(int_dy, 31)
        self.assertGreaterEqual(int_dy, 1)

        # check hour length
        self.assertEqual(len(tm[0]), 2)

        int_hr = int(tm[0])

        # check hour range
        self.assertLessEqual(int_hr, 24)
        self.assertGreaterEqual(int_hr, 1)

        # check minute length
        self.assertEqual(len(tm[1]), 2)

        int_mn = int(tm[1])

        # check minute range
        self.assertLessEqual(int_mn, 60)
        self.assertGreaterEqual(int_mn, 1)

        # check second length
        self.assertEqual(len(tm[2]), 2)

        int_sec = int(tm[2])

        # check second range
        self.assertLessEqual(int_sec, 60)
        self.assertGreaterEqual(int_sec, 1)
