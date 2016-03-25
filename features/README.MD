## Behave features and environment

> .feature - This is behave feature file. It uses BDD format to create test scenario on business logic level
Variable test parameters are present with quotas, most of them can be changed into different
values. Except for passengers which are currently set to be 3 persons maximum, adult and/or child 
only.

> environment.py - module that creates proper environment for behave. Sets-up driver and page objects and logging to be used by test script.
Currently environment parameters (such as type of browser) are hardcoded here
