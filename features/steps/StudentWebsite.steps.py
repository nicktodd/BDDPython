from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from hamcrest import assert_that, starts_with, contains_string
import time



@given(u'that I am viewing the student Web site')
def step_impl(context):
    webpage.load_webpage()

@when(u'I enter the region as \'{region}\'')
def step_impl(context, region):
    print("sorting out the region")
    webpage.region_selector.send_keys(region)
    


@when(u'I enter the machine name as \'{machine_name}\' and submit')
def step_impl(context, machine_name):
    webpage.machine_name_text_field.send_keys(machine_name)
    webpage.machine_name_text_field.send_keys(Keys.RETURN)


@then(u'the resulting page should show the message \'{message}\'')
def step_impl(context, message):
    # add a little wait in here
    WebDriverWait(webpage.driver, 3).until(EC.alert_is_present())
    alert = webpage.driver.switch_to.alert
    print(alert.text)
    assert_that(alert.text, contains_string(message))


class WebPage:

    instance = None

    def __init__(self):
       pass

    def load_webpage(self):
        chrome_options = Options()
        chrome_options.add_argument("--use-fake-ui-for-media-stream") # options turn off the prompt for the microphone
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        #chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.website = self.driver.get('https://student.conygre.com')
        delay = 3 # seconds
        WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#machineName')))
    
        self.region_selector = self.driver.find_element_by_class_name('custom-select')
        self.machine_name_text_field = self.driver.find_element_by_id('machineName')

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = WebPage()
        return cls.instance



webpage = WebPage.get_instance()



