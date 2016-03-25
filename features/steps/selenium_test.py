"""
Test steps used by behave declared here.
The most basic combination is 3 steps defined by given, when, then decorators
But behave supports also and decorator for some more elaborate tests
"""
from behave import given, when, then
from traceback import print_exc
import os
from behave.runner import Context


@given('I book from "{departure}" to "{destination}" on "{date}" for \
"{adults:d}" adults and "{child:d}" child')
def make_a_booking(context,departure,destination, date, adults, child):
    try:
        context.main_page.fill_basic_flight_info(
                                                departure_airport=departure,
                                                destination_airport=destination,
                                                flight_date=date,
                                                adults_number=adults,
                                                children_number=child)
        assert context.ticket_page.is_page_opened()
        context.ticket_page.pick_ticket_and_continue()
        assert context.reserved_seat_page.is_page_opened()
        context.reserved_seat_page.continue_to_check_out()
    except:
        print_exc(file=context.log_file)
        context.main_page.capture_screen('failure')
        raise

@when('I pay with card details "{card_number}", "{expiry_month}/{expiry_year}" \
and "{security_code}"')
def insert_card_details(context,card_number, expiry_month, expiry_year,
                        security_code):
    try:
        assert context.payment_page.is_page_opened()
        context.payment_page.fill_extra_passenger_info()
        context.payment_page.fill_card_info_and_proceed(
                                        card_number=card_number.replace(' ',''),
                                            expiry_month=expiry_month,
                                            expiry_year='20'+expiry_year,
                                            security_code=security_code)
    except:
        print_exc(file=context.log_file)
        context.main_page.capture_screen('failure')
        raise

@then('I should get payment declined message')
def check_for_declined_payment(context):
    try:
        assert context.payment_page.check_payment_error()
    except:
        print_exc(file=context.log_file)
        context.main_page.capture_screen('failure')
        raise