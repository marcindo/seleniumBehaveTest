"""
Elements that appear on choose ticket page. Each element should just have locator
(unless there is big need to use another to interact with it i.e. we need to fill text box
and close dropdown list it displays) and inherit it's own basic element type which
provides (typically one) method to interact with it
"""
from .basic_elements import TextElement
from .basic_elements import ButtonElement

from selenium.webdriver.common.by import By

class PagePreamble(TextElement):
    locator = (By.CSS_SELECTOR, ".highlighted")

class FirstRegularTicket(ButtonElement):
    locator = (By.CSS_SELECTOR, ".fare[ng-click]")

class ContinueButton(ButtonElement):
    locator = (By.CSS_SELECTOR, "button[id=continue]")