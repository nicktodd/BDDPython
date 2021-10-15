Feature: Speaking Clock
    As a user
    I want the time as text
    So that I can speak it out loud

Scenario: The time is midnight
Given the hour is '0' and the minutes are '0'
When I request the time
Then the result should be 'midnight'

Scenario: The time is midday
Given the hour is '12' and the minutes are '0'
When I request the time
Then the result should be 'midday'

