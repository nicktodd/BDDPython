import unittest
from datetime import time
from timetotext import TimeToText

class TestStringMethods(unittest.TestCase):


    def setUp(self):
        self.time_to_text=  TimeToText()

    def test_midnight(self):
        result = self.time_to_text.get_time_as_text(time(0,0,0))
        self.assertEqual("midnight", result)

    def test_midday(self):
        result = self.time_to_text.get_time_as_text(time(12,0,0))
        self.assertEqual("midday", result)


if __name__ == '__main__':
    unittest.main()


