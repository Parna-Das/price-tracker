import unittest
from validator import is_url_valid, is_frequency_valid, is_target_price_valid, is_timeout_valid, is_internet_available

class TestIsUrlValid(unittest.TestCase):
    def test_check_valid_url(self):
        actual = is_url_valid(r"https://www.amazon.in/")
        self.assertTrue(actual)
  
    def test_check_invalid_url(self):
        actual = is_url_valid(r"w.amazon.in")
        self.assertFalse(actual)

class TestfrequencyValid(unittest.TestCase):
    def test_check_frequency_lt_1_invalid(self):
        actual = is_frequency_valid(0)
        self.assertFalse(actual)

    def test_check_frequency_between_0_60_valid(self):
        actual = is_frequency_valid(7)
        self.assertTrue(actual)

    def test_check_frequency_gt_60_invalid(self):
        actual = is_frequency_valid(61)
        self.assertFalse(actual)

class TestTargetPriceValid(unittest.TestCase):
    def test_check_target_price_valid(self):
        actual = is_target_price_valid(50.000)
        self.assertTrue(actual)

    def test_check_target_price_invalid(self):
        actual = is_target_price_valid(0)
        self.assertFalse(actual)

class TestTimeoutValid(unittest.TestCase):
    def test_check_timeout_valid(self):
        actual = is_timeout_valid(5)
        self.assertTrue(actual)

    def test_check_timeout_invalid(self):
        actual = is_timeout_valid(0)
        self.assertFalse(actual)

    def test_check_timeout_invalid_gt_24(self):
        actual = is_timeout_valid(25)
        self.assertFalse(actual)

class TestInternetAvailibility(unittest.TestCase):
    def test_check_internet_available(self):
        actual = is_internet_available()
        self.assertTrue(actual)

    # Negative scenario to be written   
