import unittest
from datetime import time
from timetotext import TimeToText

class TestTimeToText(unittest.TestCase):

    def setUp(self):
        self.time_to_text = TimeToText()

    def test_midnight(self):
        # arrange / given
        
        # act / when
        result = self.time_to_text.get_time_as_text(time(0,0,0))
        # assert / then
        self.assertEqual("midnight", result)

    def test_midday(self):
        result = self.time_to_text.get_time_as_text(time(12,0,0))
        self.assertEqual("midday", result)

    def test_1am(self):
        result = self.time_to_text.get_time_as_text(time(1,0,0))
        self.assertEqual("one am", result)
        

if __name__ == '__main__':
    unittest.main()


