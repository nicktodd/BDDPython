# Created by Nick Todd at 04/10/2020
Feature: Requesting an insurance quote from a chat bot
  As a customer
  I want a quotation for car insurance
  So that I can drive my car
  
  Provided with the details for a quote, the chatbot
  should respond with a price

  Scenario: Get a Quote for someone born in 1971

    Given the user enters 'Can I have a quote'
    When asked for the make of car the user enters 'renault'
    And when asked for the model of car the user enters 'clio'
    And when asked for the engine size of car the user enters '1.2'
    And when asked when they were born the user enters '1971'
    And when asked when they passed their test the user enters '1989'
    And when prompted to confirm the user enters 'yes'
    Then the chatbot should respond with 'For driver 50 years of age who has been driving for 32 years driving a 1.2litre engine, the cost of insurance will be approximately: £53'


