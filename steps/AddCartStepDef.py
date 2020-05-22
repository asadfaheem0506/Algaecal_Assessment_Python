from behave import *
from utilities.driverUtil import driver
import utilities.config as sconfig
from pageUtils.elements import *
import re

use_step_matcher("re")

@given("I login to website")
def step_impl(context):
    driver.navigateToMaps(sconfig.website) # step to go to mentioned site

@when("I select items and add to cart")
def step_impl(context):
    driver.waitOnElement(gmail) # wait on an element when site is loaded
    driver.elementClick(gmail)  # click element when element is visible

@when("I navigate to the cart page")
def step_impl(context):
    pass
    # click element to navigate to the cart page

@then("I verify that added items are present")
def step_impl(context):
    pass
    # verify items present in cart by getting the values and doing assertion like below
    assert "value" in "output value"