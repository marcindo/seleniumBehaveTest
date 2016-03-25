"""
Elements that appear on main page. Each element should just have locator
(unless there is big need to use another to interact with it i.e. we need to fill text box
and close dropdown list it displays) and inherit it's own basic element type which
provides (typically one) method to interact with it
"""

from .basic_elements import TextBoxElement
from .basic_elements import ButtonElement
from .basic_elements import CheckBoxElement
from .basic_elements import AirPortTextBoxElement

from selenium.webdriver.common.by import By

class FirstAirportElement(object):
    locator = (By.CSS_SELECTOR, ".option[ng-class*='airportSelected']")

class FromAirportElement(AirPortTextBoxElement):
    """This class is the box element for departure airport, it also holds
    another object for the first suggested airport """
    element_from_dropdown = FirstAirportElement()
    locator = (By.CSS_SELECTOR,
               "[placeholder='Departure airport'][role='textbox']")

class ToAirportElement(AirPortTextBoxElement):
    """This class is the box element for destination airport, it also holds
    another object for the first suggested airport """
    element_from_dropdown = FirstAirportElement()
    locator = (By.CSS_SELECTOR,
               "[placeholder='Destination airport'][role='textbox']")

class OneWayCheckBox(CheckBoxElement):
    """Box to pick one-way flight only"""
    locator = (By.CSS_SELECTOR, "[value='one-way']")

class FlyOutDateDay(TextBoxElement):
    locator = (By.CSS_SELECTOR, "[ng-model='date[0]'][aria-label*='out']")

class FlyOutDateMonth(TextBoxElement):
    locator = (By.CSS_SELECTOR, "[ng-model='date[1]'][aria-label*='out']")

class FlyOutDateYear(TextBoxElement):
    locator = (By.CSS_SELECTOR, "[ng-model='date[2]'][aria-label*='out']")

class PassengersList(ButtonElement):
    locator = (By.CSS_SELECTOR, ".dropdown-handle core-icon")

class AdultsIncrement(ButtonElement):
    locator = (By.CSS_SELECTOR, "[label='Adults'] button[ng-click*='increment']")

class ChildrenIncrement(ButtonElement):
    locator = (By.CSS_SELECTOR,
               "[label='Children'] button[ng-click*='increment']")

class GoNext(ButtonElement):
    locator = (By.CSS_SELECTOR, "[ng-click*='searchFlights']")
