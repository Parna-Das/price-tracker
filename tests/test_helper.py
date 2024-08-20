import unittest
from unittest.mock import patch, MagicMock
from pathlib import Path
import sys
from helper.helper import confirm_product, start_tracking, trigger_notification, tear_down, resolve_url


class TestPriceTracker(unittest.TestCase):
    @patch('helper.helper.resolve_url')
    @patch('builtins.input', side_effect=['y'])
    @patch('helper.helper.logging')
    def test_confirm_product_positive(self, mock_logging, mock_input, mock_resolve_url):
        # Positive test case for confirm_product
        mock_resolve_url.return_value = ("Product Name", 100.0, "In Stock")
        result = confirm_product("http://amazon.in/Yonex-ZR-Aluminum-Badminton-Racquet/dp/B07SLLL3MS/ref=pd_ci_mcx_mh_pe_im_d1_hxwPPE_sspa_dk_det_p_1?pd_rd_i=B07SLLL3MS&pd_rd_w=ifKdQ&content-id=amzn1.sym.65567f53-d906-417f-bc31-6911cc9f5577&pf_rd_p=65567f53-d906-417f-bc31-6911cc9f5577&pf_rd_r=Y0T1NR5G49TA3JTSW0ZC&pd_rd_wg=Z5Mb3&pd_rd_r=16d29f98-2b95-4d4e-81d9-9fc868dd2c6d")
        self.assertTrue(result)
        mock_logging.info.assert_called_with("User opted to proceed")

    @patch('helper.helper.resolve_url')
    @patch('builtins.input', side_effect=['n'])
    @patch('helper.helper.logging')
    def test_confirm_product_negative(self, mock_logging, mock_input, mock_resolve_url):
        # Negative test case for confirm_product
        mock_resolve_url.return_value = ("Product Name", 100.0, "In Stock")
        result = confirm_product("http://amazon.in/Yonex-ZR-Aluminum-Badminton-Racquet/dp/B07SLLL3MS/ref=pd_ci_mcx_mh_pe_im_d1_hxwPPE_sspa_dk_det_p_1?pd_rd_i=B07SLLL3MS&pd_rd_w=ifKdQ&content-id=amzn1.sym.65567f53-d906-417f-bc31-6911cc9f5577&pf_rd_p=65567f53-d906-417f-bc31-6911cc9f5577&pf_rd_r=Y0T1NR5G49TA3JTSW0ZC&pd_rd_wg=Z5Mb3&pd_rd_r=16d29f98-2b95-4d4e-81d9-9fc868dd2c6d")
        self.assertFalse(result)
        mock_logging.error.assert_called_with("User requested abort")

    @patch('helper.helper.resolve_url')
    @patch('builtins.input', side_effect=['y'])
    @patch('helper.helper.logging')
    @patch('time.sleep', return_value=None)  # To avoid actual sleeping in tests
    def test_start_tracking_positive(self, mock_sleep, mock_logging, mock_input, mock_resolve_url):
        # Positive test case for start_tracking
        mock_resolve_url.return_value = ("Product Name", 50.0, "In Stock")
        result = start_tracking("http://amazon.in/Yonex-ZR-Aluminum-Badminton-Racquet/dp/B07SLLL3MS/ref=pd_ci_mcx_mh_pe_im_d1_hxwPPE_sspa_dk_det_p_1?pd_rd_i=B07SLLL3MS&pd_rd_w=ifKdQ&content-id=amzn1.sym.65567f53-d906-417f-bc31-6911cc9f5577&pf_rd_p=65567f53-d906-417f-bc31-6911cc9f5577&pf_rd_r=Y0T1NR5G49TA3JTSW0ZC&pd_rd_wg=Z5Mb3&pd_rd_r=16d29f98-2b95-4d4e-81d9-9fc868dd2c6d", 60.0)
        self.assertTrue(result)
        mock_logging.info.assert_called_with("Target price reached. \n Current price is at %s", 50.0)

    @patch('helper.helper.resolve_url')
    @patch('builtins.input', side_effect=['y', 'y'])
    @patch('helper.helper.logging')
    @patch('time.sleep', return_value=None)
    def test_start_tracking_negative_timeout(self, mock_sleep, mock_logging, mock_input, mock_resolve_url):
        # Negative test case for start_tracking (timeout)
        mock_resolve_url.return_value = ("Product Name", 100.0, "In Stock")
        result = start_tracking("http://amazon.in/Yonex-ZR-Aluminum-Badminton-Racquet/dp/B07SLLL3MS/ref=pd_ci_mcx_mh_pe_im_d1_hxwPPE_sspa_dk_det_p_1?pd_rd_i=B07SLLL3MS&pd_rd_w=ifKdQ&content-id=amzn1.sym.65567f53-d906-417f-bc31-6911cc9f5577&pf_rd_p=65567f53-d906-417f-bc31-6911cc9f5577&pf_rd_r=Y0T1NR5G49TA3JTSW0ZC&pd_rd_wg=Z5Mb3&pd_rd_r=16d29f98-2b95-4d4e-81d9-9fc868dd2c6d", 50.0, timeout=0)
        self.assertFalse(result)
        mock_logging.warning.assert_called_with("Triggering timeout of - '%s' hours", 0)
        with self.assertRaises(KeyboardInterrupt):
            start_tracking(url=r'https://www.amazon.in/', target_price=1049.00, frequency=10, timeout=10)

    @patch('helper.helper.AudioPlayer')
    @patch('helper.helper.logging')
    def test_trigger_notification_positive(self, mock_logging, mock_audio_player):
        # Positive test case for trigger_notification
        mock_player_instance = MagicMock()
        mock_audio_player.return_value = mock_player_instance

        trigger_notification()
        mock_player_instance.play.assert_called_once_with(block=True)
        mock_logging.info.assert_called_with("Successfully notified user using file - '%s'", Path("notification.mp3"))

    @patch('helper.helper.AudioPlayer')
    @patch('helper.helper.logging')
    def test_trigger_notification_negative(self, mock_logging, mock_audio_player):
        # Negative test case for trigger_notification
        mock_audio_player.side_effect = FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            trigger_notification()

    @patch('helper.helper.sys.exit')
    def test_tear_down(self, mock_exit):
        # Test for tear_down
        tear_down()
        mock_exit.assert_called_once_with(0)

    @patch('helper.helper.requests.get')
    @patch('helper.helper.bs')
    @patch('helper.helper.logging')
    def test_resolve_url_positive(self, mock_logging, mock_bs, mock_requests_get):
        # Positive test case for resolve_url
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_requests_get.return_value = mock_response

        mock_soup = MagicMock()
        mock_bs.return_value = mock_soup

        mock_soup.find.side_effect = [
            MagicMock(text="Product Name"),
            MagicMock(text="1049.00"),
            MagicMock(text="In Stock")
        ]

        result = resolve_url("http://amazon.in/Yonex-ZR-Aluminum-Badminton-Racquet/dp/B07SLLL3MS/ref=pd_ci_mcx_mh_pe_im_d1_hxwPPE_sspa_dk_det_p_1?pd_rd_i=B07SLLL3MS&pd_rd_w=ifKdQ&content-id=amzn1.sym.65567f53-d906-417f-bc31-6911cc9f5577&pf_rd_p=65567f53-d906-417f-bc31-6911cc9f5577&pf_rd_r=Y0T1NR5G49TA3JTSW0ZC&pd_rd_wg=Z5Mb3&pd_rd_r=16d29f98-2b95-4d4e-81d9-9fc868dd2c6d")
        self.assertEqual(result, ("Product Name", 1049.00, "In Stock"))
        mock_logging.info.assert_called_with("URL - '%s' resolved with status code 200", "http://amazon.in/Yonex-ZR-Aluminum-Badminton-Racquet/dp/B07SLLL3MS/ref=pd_ci_mcx_mh_pe_im_d1_hxwPPE_sspa_dk_det_p_1?pd_rd_i=B07SLLL3MS&pd_rd_w=ifKdQ&content-id=amzn1.sym.65567f53-d906-417f-bc31-6911cc9f5577&pf_rd_p=65567f53-d906-417f-bc31-6911cc9f5577&pf_rd_r=Y0T1NR5G49TA3JTSW0ZC&pd_rd_wg=Z5Mb3&pd_rd_r=16d29f98-2b95-4d4e-81d9-9fc868dd2c6d")

    @patch('helper.helper.requests.get')
    @patch('helper.helper.logging')
    def test_resolve_url_negative(self, mock_logging, mock_requests_get):
        # Negative test case for resolve_url
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_requests_get.return_value = mock_response

        with self.assertRaises(KeyboardInterrupt):
            resolve_url("http://amazon.in/Yonex-ZR-Aluminum-Badminton-Racquet/dp/B07SLLL3MS/ref=pd_ci_mcx_mh_pe_im_d1_hxwPPE_sspa_dk_det_p_1?pd_rd_i=B07SLLL3MS&pd_rd_w=ifKdQ&content-id=amzn1.sym.65567f53-d906-417f-bc31-6911cc9f5577&pf_rd_p=65567f53-d906-417f-bc31-6911cc9f5577&pf_rd_r=Y0T1NR5G49TA3JTSW0ZC&pd_rd_wg=Z5Mb3&pd_rd_r=16d29f98-2b95-4d4e-81d9-9fc868dd2c6d")
        mock_logging.error.assert_called_with("Failed to resolve URL with status code of - %s ", 404)