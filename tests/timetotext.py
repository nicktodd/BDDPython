class TimeToText:

    def __init__(self):
        pass

    def get_time_as_text(self, time_to_convert):
        if time_to_convert.hour == 0 and time_to_convert.minute == 0 :
            return "midnight"
        elif time_to_convert.hour == 12 and time_to_convert.minute == 0 :
            return "midday"
        else:
            return None
