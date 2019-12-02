import unittest
import Forecast

class TestForecast(unittest.TestCase):

    def test_read_api(self):
        resp = Forecast.api_read()
        self.assertIsInstance(resp, str)


if __name__ == '__main__':
    unittest.main()






