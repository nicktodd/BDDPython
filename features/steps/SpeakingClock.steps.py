from datetime import time
from behave import given, when, then 
from hamcrest import assert_that, equal_to


@given(u'the hour is \'{hour}\' and the minutes are \'{minutes}\'')
def step_impl(context, hour, minutes):
    context.time_to_text = TimeToText()
    context.provided_time = time(int(hour),int(minutes),0)    


@when(u'I request the time')
def step_impl(context):
    context.result = context.time_to_text.get_time_as_text(context.provided_time)   

@then(u'the result should be \'{expected_result}\'')
def step_impl(context, expected_result):
    assert_that(context.result, equal_to(expected_result))



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
