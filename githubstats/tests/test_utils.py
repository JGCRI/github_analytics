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
