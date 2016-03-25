"""
Elements that appear on payment page. Each element should just have locator
(unless there is big need to use another to interact with it i.e. we need to fill text box
and close dropdown list it displays) and inherit it's own basic element type which
provides (typically one) method to interact with it
"""

from .basic_elements import ButtonElement
from .basic_elements import TextElement
from .basic_elements import MultipleTextBoxElement
from .basic_elements import CheckBoxElement
from .basic_elements import TextBoxElementWithScroll
from .basic_elements import TextBoxElementWithScrollAndActionChain

from selenium.webdriver.common.by import By

class PassengerDetailsTitle(TextElement):
    locator = (By.CSS_SELECTOR, "[translate*='passenger_details']")

class PassengersTitle(MultipleTextBoxElement):
    """All text boxes with passenger title"""
    locator = (By.CSS_SELECTOR, "[name*='title']")

class PassengersName(MultipleTextBoxElement):
    """All text boxes with passenger first name"""
    locator = (By.CSS_SELECTOR, "[name*='firstName']")

class PassengersLastName(MultipleTextBoxElement):
    """All text boxes with passenger last name"""
    locator = (By.CSS_SELECTOR, "[name*='lastName']")

class EmailAddres(TextBoxElementWithScroll):
    locator = (By.CSS_SELECTOR, "[name='emailAddress']")

class PhoneNumberCountry(TextBoxElementWithScroll):
    locator = (By.CSS_SELECTOR, "[name='phoneNumberCountry']")

class PhoneNumber(TextBoxElementWithScrollAndActionChain):
    locator = (By.CSS_SELECTOR, "[name='phoneNumber']")

class CardNumber(TextBoxElementWithScroll):
    locator = (By.CSS_SELECTOR, "[name='cardNumber']")

class CardType(TextBoxElementWithScroll):
    locator = (By.CSS_SELECTOR, "[name='cardType']")

class ExpiryMonth(TextBoxElementWithScroll):
    locator = (By.CSS_SELECTOR, "[name='expiryMonth']")

class ExpiryYear(TextBoxElementWithScroll):
    locator = (By.CSS_SELECTOR, "[name='expiryYear']")

class SecurityCode(TextBoxElementWithScroll):
    locator = (By.CSS_SELECTOR, "[name='securityCode']")

class CardHolder(TextBoxElementWithScroll):
    locator = (By.CSS_SELECTOR, "[name='cardHolderName']")

class BillingAdress(TextBoxElementWithScroll):
    locator = (By.CSS_SELECTOR, "[name='billingAddressAddressLine1']")

class BillingAdressCity(TextBoxElementWithScroll):
    locator = (By.CSS_SELECTOR, "[name='billingAddressCity']")

class BillingAdressPostCode(TextBoxElementWithScroll):
    locator = (By.CSS_SELECTOR, "[name='billingAddressPostcode']")

class AcceptPolicyCheckBox(CheckBoxElement):
    locator = (By.CSS_SELECTOR, "[name='acceptPolicy']")

class PayNowButton(ButtonElement):
    locator = (By.CSS_SELECTOR, "[translate*='pay_now']")

class PaymentError(TextElement):
    locator = (By.CSS_SELECTOR, "[translate*=error_title]")
