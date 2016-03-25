"""
Basic generic elements classes. Separate any actual selenium
methods here.
This elements types are inherited by real page elements, and provide
selenium functionality for them using their locators.
The most basic element types are TextBox, Button, CheckBox and Text
is some real element does not work with them and requires some selenium tricks
and modifications, create modified basic type for it
That way can ensure that special modifications won't affect other elements
which were working fine, and allows to easy keep track which elements
required changes.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class TextBoxElement(object):
    """Base element class for text box type of elemenets."""

    def fill_box(self, obj, value):
        """Fill text box with value, clear any pre-filled value."""
        browser = obj.browser
        WebDriverWait(browser, 10).until(
            lambda browser: browser.find_element(*self.locator)).clear()
        browser.find_element(*self.locator).send_keys(value)


class TextBoxElementWithScroll(object):
    """Modyified version of text box element that also scrolls element into view
    It should happen automatically with selenium 2 but some browsers and drivers are
    buggy with that"""
    def fill_box(self, obj, value):
        """Fill text box with value, scroll to the box if it's not visible
        Use action chains as phone number field does not work with send_keys"""
        browser = obj.browser
        element = browser.find_element(*self.locator)
        browser.execute_script("arguments[0].scrollIntoView(true);", element)
        wait=WebDriverWait(browser, 10)
        element = wait.until(EC.visibility_of_element_located(self.locator))
        browser.find_element(*self.locator).send_keys(value)


class TextBoxElementWithScrollAndActionChain(object):
    """Object specifically made for one text box that need action chains
    because regular send_keys does not work
    - affects PhoneNumber box on payment page"""
    def fill_box(self, obj, value):
        """Fill text box with value, scroll to the box if it's not visible
        Use action chains as phone number field does not work with send_keys"""
        browser = obj.browser
        element = browser.find_element(*self.locator)
        browser.execute_script("arguments[0].scrollIntoView(true);", element)
        wait = WebDriverWait(browser, 10)
        element = wait.until(EC.visibility_of_element_located(self.locator))
        element.click()
        action = ActionChains(browser)
        action.send_keys(value)
        action.perform()


class AirPortTextBoxElement(object):
    """Airport text boxes behave strangely - they display dropdown list from which suggested
     airport needs to be chosen, and typing 3-letter code for airport also requires pressing
     arrow key otherwise suggestion is not displayed. Those are some selenium sheaningans as they
     don't happen when manually controling app. Hence fill_box function is different for them"""
    def fill_box(self, obj, value):
        """Fill text box with value, clear any pre-filled value. This function
        also presses one option from dropdown list to hide it  the text to the
        value supplied"""
        browser = obj.browser
        wait = WebDriverWait(browser, 10)
        element = wait.until(EC.visibility_of_element_located(self.locator))
        element.clear()
        action = ActionChains(browser)
        action.send_keys(value)
        #add left arrow key otherwise suggestion for destination airport might
        #not appear
        action.send_keys(Keys.ARROW_LEFT)
        action.perform()
        # pick one choice from the dropdown list - usually needed to get rid of
        # the list, otherwise app doesn't behave properly
        element = wait.until(EC.element_to_be_clickable(
                                           self.element_from_dropdown.locator))
        element.click()


class MultipleTextBoxElement(object):
    """Basic element for situations when same text box type is repeated more than once
    on page, i.e. passenger name fields for each passenger. Instead of filling them separately
    map each box to the corresponding value. Works even if element list and values list are not
    equal in size, as it will just ignore any extras"""
    def fill_box(self, obj, value_list):
        """Fill text box with value, clear any pre-filled value."""
        browser = obj.browser
        # create pairs of (box_element, valie to fill in box) using zip()
        # seach for all fields of given type and map them to
        # corresponding values. If one of the lists is longer than other it should
        # ignore any extra values
        [element.send_keys(value) for element,value in
         zip(browser.find_elements(*self.locator),value_list)]


class ButtonElement(object):
    """Base element class for button type of elements"""
    def press_button(self, obj):
        """wait for button to be clickable, then press it"""
        browser = obj.browser
        wait = WebDriverWait(browser, 10)
        button = wait.until(EC.element_to_be_clickable(self.locator))
        button.click()


class CheckBoxElement(object):
    """Check box type element that can be clicked, but selenium doesn't recognize
    it as regular buttons"""
    def check_box(self, obj):
        browser = obj.browser
        browser.find_element(*self.locator).click()


class TextElement(object):
    """Base element class for text-only type of elements"""
    def get_text(self, obj):
        """Wait till element with text appears and return this text, otherwise
        raise error"""
        browser = obj.browser
        WebDriverWait(browser, 30).until(
            lambda browser: browser.find_element(*self.locator).text)
        return browser.find_element(*self.locator).text

    def check_text(self, obj):
        """Same as above, except returns true if locator just has any text, used
        when only want to know if element appeared and has text"""
        browser = obj.browser
        WebDriverWait(browser, 30).until(
            lambda browser: browser.find_element(*self.locator).text)
        return True
