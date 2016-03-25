'''
Module that sets environment for behave
'''
from selenium import webdriver
from behave.log_capture import capture
from pages import MainPage, TicketPage, ReservedSeatPage, PaymentPage

import os
import sys
from datetime import datetime

@capture
def before_all(context):
    context.config.setup_logging()
    context.browser = webdriver.Firefox()
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    context.log_directory= os.path.dirname(__file__)+ \
'\\..\\logs\\{}\\'.format(now)
    if not os.path.exists(context.log_directory):
        os.makedirs(context.log_directory)
    context.log_file = open(context.log_directory+'log-{}.log'.format(now), 'w')

@capture
def before_feature(context,feature):
    context.browser.get('http://Ryanair.com/ie/en/')
    context.main_page = MainPage(context.browser, context.log_directory)
    context.ticket_page = TicketPage(context.browser, context.log_directory)
    context.reserved_seat_page = ReservedSeatPage(context.browser,
                                                  context.log_directory)
    context.payment_page = PaymentPage(context.browser, context.log_directory)
    context.log_file.write('{!s} \t#{}:{}\n'.format(feature.name, feature.filename, feature.line))

@capture
def before_scenario(context,scenario):
    context.log_file.write('\t{!s} \t#{}:{}\n'.format(scenario.name, scenario.filename, scenario.line))

@capture
def before_step(context,step):
    context.log_file.write('\t\t{!s} \t#{}:{}\n'.format(step.name, step.filename, step.line))

@capture
def after_step(context,step):
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    context.browser.get_screenshot_as_file(context.log_directory+
step.keyword+'{}.png'.format(now))
    context.log_file.write('\t\tstep: {!s}\n'.format(step.status))

@capture
def after_scenario(context,scenario):
    context.log_file.write('\tScenario: {!s} Time taken: {!s}\n'.format(scenario.status, scenario.duration))

@capture
def after_feature(context,feature):
    context.log_file.write('Whole feature: {!s} Time taken: {!s}\n'.format(feature.status, feature.duration))

@capture
def after_all(context):
    context.browser.quit()
    context.log_file.close()


