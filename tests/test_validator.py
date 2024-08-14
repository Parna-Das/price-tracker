"""Test file to verify all the function in validation"""

import unittest
from validator import is_url_valid, is_frequency_valid, is_target_price_valid, is_timeout_valid, is_internet_available


class TestIsUrlValid(unittest.TestCase):
    """Unit test class to verify if URL is valid

    Args:
        unittest (_type_): unit test
    """

    def test_check_valid_url(self):
        """Method to verify if URL is valid"""
        actual = is_url_valid(r"https://www.amazon.in/")
        self.assertTrue(actual)

    def test_check_invalid_url(self):
        """Method to verify if URL is invalid"""
        actual = is_url_valid(r"w.amazon.in")
        self.assertFalse(actual)


class TestfrequencyValid(unittest.TestCase):
    """Unit test class to verify if frequency is valid

    Args:
        unittest (_type_): unit test
    """

    def test_check_frequency_lt_1_invalid(self):
        """Method to verify if frequency is valid"""
        actual = is_frequency_valid(0)
        self.assertFalse(actual)

    def test_check_frequency_between_0_60_valid(self):
        """Method to verify if frequency is valid"""
        actual = is_frequency_valid(7)
        self.assertTrue(actual)

    def test_check_frequency_gt_60_invalid(self):
        """Method to verify if frequency is valid"""
        actual = is_frequency_valid(61)
        self.assertFalse(actual)


class TestTargetPriceValid(unittest.TestCase):
    """Unit test class to verify if target price is valid

    Args:
        unittest (_type_): unit test
    """

    def test_check_target_price_valid(self):
        """Method to verify if target price is valid"""
        actual = is_target_price_valid(50.000)
        self.assertTrue(actual)

    def test_check_target_price_invalid(self):
        """Method to verify if target price is valid"""
        actual = is_target_price_valid(0)
        self.assertFalse(actual)


class TestTimeoutValid(unittest.TestCase):
    """Unit test class to verify if timeout is valid

    Args:
        unittest (_type_): unit test
    """

    def test_check_timeout_valid(self):
        """Method to verify if timeout is valid"""
        actual = is_timeout_valid(5)
        self.assertTrue(actual)

    def test_check_timeout_invalid(self):
        """Method to verify if target price is valid"""
        actual = is_timeout_valid(0)
        self.assertFalse(actual)

    def test_check_timeout_invalid_gt_24(self):
        """Method to verify if target price is valid"""
        actual = is_timeout_valid(25)
        self.assertFalse(actual)


class TestInternetAvailibility(unittest.TestCase):
    """Unit test class to verify if internet is available

    Args:
        unittest (_type_): unit test
    """

    def test_check_internet_available(self):
        """Unit test class to verify if internet is available"""
        actual = is_internet_available()
        self.assertTrue(actual)

    # Negative scenario to be written
