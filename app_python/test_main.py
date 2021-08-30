import unittest
import main

from datetime import datetime
from pytz import timezone


class TestAppPython(unittest.TestCase):
    def setUp(self):
        main.app.testing = True
        self.app = main.app.test_client()

    def test_moscow_time(self):
        self.assertEqual(main.moscow_time().replace(microsecond=0), datetime.now(
            timezone('Europe/Moscow')).time().replace(microsecond=0))

    def test_index(self):
        self.assertIn(datetime.now(
            timezone('Europe/Moscow')).time().strftime("%H:%M:%S"), main.index())

    def test_home(self):
        self.assertTrue(self.app.get('/'))
