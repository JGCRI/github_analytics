import unittest

import githubstats.utils as u


class TestUtils(unittest.TestCase):
    """Test `utils.py` functions."""

    def test_leading_zero(self):
        """Check the number of months in the working hours file derived list."""

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
