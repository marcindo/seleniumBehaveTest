Feature: booking flights 

  Scenario: Try to book flight up to declined payment
     Given I book from "DUB" to "AMS" on "11/04/2016" for "2" adults and "1" child
      when I pay with card details "5555 5555 5555 5557", "10/18" and "265"
      then I should get payment declined message
