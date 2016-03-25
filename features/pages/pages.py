'''
Module with all separate page objects.
Each page first imports a set of it's elements, and holds
private methods as wrappers for accessing their elements methods,
as well as high level wrappers called by test steps.
The advantage of this structure is that it's very easy to read
what actions are performed on each page
'''
import time
from datetime import datetime

from .elements import main_page_elements as main_elements
from .elements import payment_page_elements as payment_elements
from .elements import reserved_seat_page_elements as reserved_elements
from .elements import ticket_page_elements as ticket_elements


class SeleniumPage:
    def __init__(self, browser, log_directory):
        self.browser = browser
        self.log_directory = log_directory

    def capture_screen(self,name=None):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        self.browser.get_screenshot_as_file(self.log_directory+\
'{0}_{1}.png'.format(name,now))


class MainPage(SeleniumPage):
    """Home page action methods come here"""
    # page elements
    from_airport_element = main_elements.FromAirportElement()
    to_airport_element = main_elements.ToAirportElement()
    one_way_checkbox = main_elements.OneWayCheckBox()
    # flight date is actually a set of 3 elements, but save them all
    # in one list so we can easily map date values to them
    fly_out_date = (main_elements.FlyOutDateDay(),
                    main_elements.FlyOutDateMonth(),
                    main_elements.FlyOutDateYear())
    passenger_list = main_elements.PassengersList()
    adults_increment = main_elements.AdultsIncrement()
    children_increment = main_elements.ChildrenIncrement()
    go_next_button = main_elements.GoNext()

    #Declares a variable that will contain the retrieved text
    def __fill_departure_airport(self, airport_name):
        self.from_airport_element.fill_box(self, airport_name)

    def __fill_destination_airport(self, airport_name):
        self.to_airport_element.fill_box(self, airport_name)

    def __check_one_way(self):
        self.one_way_checkbox.check_box(self)

    def __fill_flyout_date(self, date):
        """date is in d/m/y format so first split it into 3 values
         then simply create list of pairs using zip(), where each date element
         in text box has corresponding date value"""
        date_list = date.split('/')
        [element.fill_box(self, value) for element,value in
         zip(self.fly_out_date, date_list)]

    def __fill_passengers(self, adults_number, children_number):
        self.passenger_list.press_button(self)
        # there is always one adult pre-added so reduce required amount of one
        for amount in range(adults_number-1):
            self.adults_increment.press_button(self)
        for amount in range(children_number):
            self.children_increment.press_button(self)

    def __press_go_next_button(self):
        self.go_next_button.press_button(self)

    def fill_basic_flight_info(self, departure_airport, destination_airport,
                               flight_date, adults_number, children_number):
        """Fill basic booking info on main page, start and end airport
        date and number of passangers, then proceed further"""
        self.__fill_departure_airport(departure_airport)
        self.__fill_destination_airport(destination_airport)
        self.__check_one_way()
        self.__fill_flyout_date(flight_date)
        self.__fill_passengers(adults_number, children_number)
        self.__press_go_next_button()

class TicketPage(SeleniumPage):
    """Page with choice for tickets that appears after first
    part of booking is done main page"""
    # page elements
    page_preamble = ticket_elements.PagePreamble()
    first_available_ticket = ticket_elements.FirstRegularTicket()
    continue_button = ticket_elements.ContinueButton()

    def __pick_first_ticket(self):
        self.first_available_ticket.press_button(self)

    def __press_continue_button(self):
        self.continue_button.press_button(self)

    def is_page_opened(self):
        """look for specific text, and check if it equals value read from
        element"""
        return self.page_preamble.check_text(self)

    def pick_ticket_and_continue(self):
        """Just pick first ticket that is available then press continue"""
        self.__pick_first_ticket()
        time.sleep(1) #  HACK: there is small animation before button is
                    # actually clickable but selenium doesn't catch that
        self.__press_continue_button()


class ReservedSeatPage(SeleniumPage):
    """Page for reserving"""
    reserve_seat_advert_title =reserved_elements.ReserveSeatAdvertTitle()
    reserve_seat_advert_close = reserved_elements.ReserveSeatAdvertCloseButton()
    check_out_button = reserved_elements.CheckOutButton()

    def __close_reserve_seat_advert(self):
        self.reserve_seat_advert_close.press_button(self)

    def __press_checkout_button(self):
        self.check_out_button.press_button(self)

    def is_page_opened(self):
        """look for specific text, and check if it equals value read from
        element"""
        return "Reserve seat" in self.reserve_seat_advert_title.get_text(self)

    def continue_to_check_out(self):
        self.__close_reserve_seat_advert()
        time.sleep(1) #  HACK: small delay before dialog window disappers
        self.__press_checkout_button()

class PaymentPage(SeleniumPage):
    """Page with all passenger, booking and payment details"""
    # page elements
    passenger_detail_title = payment_elements.PassengerDetailsTitle()
    pay_now_button = payment_elements.PayNowButton()
    accepy_policy_checkbox = payment_elements.AcceptPolicyCheckBox()
    payment_error = payment_elements.PaymentError()
    # define dicts of different elements to be filled, so we can easily map them
    # with corresponding values to fill
    passengers_info_elements = dict(
        titles=payment_elements.PassengersTitle(),
        names=payment_elements.PassengersName(),
        lastNames=payment_elements.PassengersLastName(),
    )
    booking_info_elements = dict(
        email=payment_elements.EmailAddres(),
        phoneNumber=payment_elements.PhoneNumber(),
        phoneNumberCountry=payment_elements.PhoneNumberCountry(),
        billingAddress=payment_elements.BillingAdress(),
        billingAdressCity=payment_elements.BillingAdressCity(),
        billingAdressPostCode=payment_elements.BillingAdressPostCode(),
    )
    card_info_elements = dict(
        card_number=payment_elements.CardNumber(),
        card_type=payment_elements.CardType(),
        expiry_month=payment_elements.ExpiryMonth(),
        expiry_year=payment_elements.ExpiryYear(),
        security_code=payment_elements.SecurityCode(),
        card_holder=payment_elements.CardHolder(),
    )
    # define dicts of values to fill the text boxes, keep key names same as
    # in the dicts above

    #note that this list currently supports exactly 3 passengers
    passengers_info = dict(
        titles=['Mr', 'Mrs', 'Ms'],
        names=['John', 'Jane', 'Alice'],
        lastNames=['Smith', 'Smith', 'Smith'],
    )
    booking_info = dict(
        email="JohnSmith@gmail.com",
        phoneNumber='99999999',
        phoneNumberCountry='Ireland',
        billingAddress='21 Sun Lane',
        billingAdressCity='Dublin',
        billingAdressPostCode='12345',
    )
    card_info = dict(
        card_number='9999 9999 9999 9999',
        card_type='MasterCard',
        expiry_month='01',
        expiry_year='2020',
        security_code='999',
        card_holder='John Smith',
    )

    def __fill_passengers_info(self):
        """just go through all box elements from elements dict and fill
        them with corresponding values from info dict"""
        for key in self.passengers_info_elements:
            self.passengers_info_elements[key].fill_box(self,
                                                    self.passengers_info[key])

    def __fill_booking_info(self):
        """just go through all box elements from elements dict and fill
        them with corresponding values from info dict"""
        for key in self.booking_info_elements:
            self.booking_info_elements[key].fill_box(self,
                                                    self.booking_info[key])

    def __fill_card_info(self):
        """just go through all box elements from elements dict and fill
        them with corresponding values from info dict"""
        for key in self.card_info_elements:
            self.card_info_elements[key].fill_box(self,
                                                    self.card_info[key])

    def __press_pay_now_button(self):
        self.pay_now_button.press_button(self)

    def __accept_terms_and_conditions(self):
        self.accepy_policy_checkbox.check_box(self)

    def is_page_opened(self):
        """look for specific text, and check if it equals value read from
        element"""
        return "Passenger details" in self.passenger_detail_title.get_text(self)

    def fill_extra_passenger_info(self):
        self.__fill_passengers_info()
        self.__fill_booking_info()

    def fill_card_info_and_proceed(self,card_number=None, card_type=None,
    expiry_month=None, expiry_year=None, security_code=None, card_holder=None):
        #save all arguments with their names as dict
        args = locals()
        #replace default values by keys that were passed to the function
        for key in args:
            if args[key] and key != 'self':
                self.card_info[key]=args[key]
        self.__fill_card_info()
        self.__accept_terms_and_conditions()
        self.__press_pay_now_button()

    def check_payment_error(self):
        return "problem" in self.payment_error.get_text(self)
