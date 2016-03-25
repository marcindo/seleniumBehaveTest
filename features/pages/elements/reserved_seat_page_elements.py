"""
Elements that appear on reserve seat page. Each element should just have locator
(unless there is big need to use another to interact with it i.e. we need to fill text box
and close dropdown list it displays) and inherit it's own basic element type which
provides (typically one) method to interact with it
"""

from .basic_elements import TextElement
from .basic_elements import ButtonElement

from selenium.webdriver.common.by import By

class ReserveSeatAdvertTitle(TextElement):
    locator = (By.CSS_SELECTOR, ".dialog-title-left")

class ReserveSeatAdvertCloseButton(ButtonElement):
    locator = (By.CSS_SELECTOR, "[icon-id*='close']")

class CheckOutButton(ButtonElement):
    locator = (By.CSS_SELECTOR, "button[ng-click*=Continue]")

