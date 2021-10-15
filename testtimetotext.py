from unittest import TestCase
from datetime import time

class TestTimeToText(TestCase):

    # fixtures
    converter = None

    def setUp(self):
        self.converter = TimeToTextConverter()
        print("in setup")



    def test_can_do_midnight(self):
        # when / act
        result = self.converter.time_to_text(time(0,0))
        # then / assert
        self.assertEquals("midnight", result)


    def test_can_do_midday(self):
        # when / act
        result = self.converter.time_to_text(time(12,0))
        # then / assert
        self.assertEquals("midday", result)

class TimeToTextConverter:

    def __init__(self):
        pass

    def time_to_text(self, time_to_convert):
        if time_to_convert.hour == 0 and time_to_convert.minute == 0:
            return "midnight"
        elif time_to_convert.hour == 12 and time_to_convert.minute == 0:
            return "midday"
        else:
            return None

