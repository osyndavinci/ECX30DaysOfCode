# python | Day 10
# USSD Bank Service
# Task: Create a mock USSD service that takes user input, and provides appropriate response. Description:
# *User provides a USSD code as input *User can then choose among a list of options(with numbers),
# whether to check balance, send money, purchase airtime, etc.
# *For check balance, the user is prompted to provide his password (hard-coded by you.).
# If correct, s/he is shown the balance-also hard coded.
# *For sending money, the user is prompted to choose from a selection of banks,
# after which he provides an account number, and then an amount to send. And then a password,
# which if correct, would send the required amount, and deduct from account balance.
# *Follow a similar scheme as sending money, for purchasing airtime-except that in this case,
# the user is ported for a phone number instead.


def mock_ussd():
    balance = 100000
    pin = 2002
    ussd_code = "*737#"
    user_input = str(input("Enter USSD code: "))
    if ussd_code == user_input:
        try:
            x = int(input("""1.Airtime-Self
2.Airtime-Others
3.Data
4.Check balance
5.Transfer 
6.Cable TV
7.Pay Bills
8.Next
--->: """))
            if x == 1:
                amount = int(input("Please enter amount: "))
                if amount < balance:
                    print("Transaction Successful! "
                          "You have successfully recharged your line with N{} worth of airtime.".format(amount))
                    balance -= amount
                else:
                    print("You do not have sufficient fund to complete this transaction.")

            elif x == 2:
                number = int(input("Please enter 3rd party mobile: "))
                amount = int(input("Please enter amount: "))
                entered_pin = int(input("Enter your 737 PIN or Token code to Top Up {} with NGN {} or "
                                        "enter 0 to cancel".format(number, amount)))
                if entered_pin == pin and amount < balance:
                    print("Transaction Successful! "
                          "You have successfully purchased N{} worth of airtime for {}.".format(amount, number))
                    balance -= amount
                elif entered_pin != pin:
                    print("Sorry, your PIN is incorrect! Please try again.")
                elif amount > balance:
                    print("You do not have sufficient fund to complete this transaction.")
                elif entered_pin == 0:
                    print("You canceled this transaction. No money was debited.")

            elif x == 3:
                choice = int(input("Purchase Data for: \n    1. Self \n    2. 3rd Party \n    --->: "))
                if choice == 1:
                    plan = int("Please select a Data plan: \n    1. 1gb for N500 \n    2. 6gb for N1500 "
                               "\n    3. 10gb for N3500")
                    if plan == 1:
                        amount = 500
                        if amount < balance:
                            print("Transaction Successful! "
                                  "You have successfully purchased 1gb worth of Data for N{}.".format(amount))
                            balance -= amount
                        else:
                            print("You do not have sufficient fund to complete this transaction.")
                    if plan == 2:
                        amount = 1500
                        if amount < balance:
                            print("Transaction Successful! "
                                  "You have successfully purchased 6gb worth of Data for N{}.".format(amount))
                            balance -= amount
                        else:
                            print("You do not have sufficient fund to complete this transaction.")
                    if plan == 3:
                        amount = 3500
                        if amount < balance:
                            print("Transaction Successful! "
                                  "You have successfully purchased 10gb worth of Data for N{}.".format(amount))
                            balance -= amount
                        else:
                            print("You do not have sufficient fund to complete this transaction.")
                elif choice == 2:
                    entered_pin = int(input("Enter your 737 PIN or Token code to continue"))
                    if entered_pin == pin:
                        m_network = {1: "an MTN", 2: "a GLO", 3: "an Airtel", 4: "a 9mobile"}
                        network = int(input("Please select mobile network: \n    1. MTN \n    2. GLO "
                                            "\n     3. Airtel \n    4. 9mobile"))
                        number = int(input("Please enter 3rd party mobile: "))
                        plan = int("Please select {} Data plan: \n    1. 1gb for N500 \n    2. 6gb for N1500 "
                                   "\n    3. 10gb for N3500".format(m_network[network]))

                        if plan == 1:
                            amount = 500
                            if amount < balance:
                                print("Transaction Successful! "
                                      "You have successfully purchased 1gb worth of Data at N{}"
                                      "for {}.".format(amount, number))
                                balance -= amount
                            else:
                                print("You do not have sufficient fund to complete this transaction.")
                        elif plan == 2:
                            amount = 1500
                            if amount < balance:
                                print("Transaction Successful! "
                                      "You have successfully purchased 6gb worth of Data at N{}"
                                      "for {}.".format(amount, number))
                                balance -= amount
                            else:
                                print("You do not have sufficient fund to complete this transaction.")
                        elif plan == 3:
                            amount = 3500
                            if amount < balance:
                                print("Transaction Successful! "
                                      "You have successfully purchased 10gb worth of Data at N{}"
                                      "for {}.".format(amount, number))
                                balance -= amount
                            else:
                                print("You do not have sufficient fund to complete this transaction.")
                else:
                    print("Invalid option entered, please try again")
            elif x == 4:
                entered_pin = int(input("Please Enter your 737 PIN at N10 charge to confirm or 0 to cancel \n--->: "))
                if entered_pin == pin:
                    print("Your account balance is N{}".format(balance - 10))
                else:
                    print("Sorry, your PIN is incorrect! Please try again.")

            elif x == 5:
                choice = int(input("Select bank: \n    1. First bank \n    2. Access (Diamond) "
                                   "\n    3. Access \n    4. Zenith \n    5. UBA "
                                   "\n    6. Ecobank \n    7. Polaris Bank \n    8. FCMB \n    --->: "))
                if 0 < choice < 9:    # chooses any of the banks just for sample
                    name = "Roy Williams"
                    acc_number = int(input("Enter account number: "))
                    amount = int(input("Enter amount: "))
                    entered_pin = int(input("Please Enter your 737 PIN to send N{} to {} with account number {}"
                                            " at N3.15 charge  or 0 to cancel".format(amount, name, acc_number)))
                    if entered_pin == pin and amount < balance:
                        print("Transaction Successful! "
                              "You have successfully sent N{} to {}.".format(amount, name))
                        balance -= (amount + 3.15)
                    elif entered_pin != pin:
                        print("Sorry, your PIN is incorrect! Please try again.")
                    elif amount > balance:
                        print("You do not have sufficient fund to complete this transaction.")
                    elif entered_pin == 0:
                        print("You canceled this transaction. No money was debited.")
                else:
                    print("Invalid option entered, please try again")

            elif x == 6:
                sc_number = int(input("Please enter your Smart Card Number: "))
                choice = int(input("Please select : \n    1. Renewal \n    2. New Request"))
                if choice == 1:
                    amount = 3600
                    entered_pin = int(input("Enter your 737 PIN or Token code to Top Up your smart card number {} "
                                            "with NGN {} at N5.52 charge or "
                                            "enter 0 to cancel".format(sc_number, amount)))
                    if entered_pin == pin and amount < balance:
                        print("Transaction Successful! "
                              "You have successfully recharged your Cable TV with N{}.".format(amount))
                        balance -= (amount + 5.52)
                    elif entered_pin != pin:
                        print("Sorry, your PIN is incorrect! Please try again.")
                    elif amount > balance:
                        print("You do not have sufficient fund to complete this transaction.")
                    elif entered_pin == 0:
                        print("You canceled this transaction. No money was debited.")
                elif choice == 2:
                    print("Please go to your nearest cable Cable TV to request a new registration.")
                else:
                    print("Invalid option entered, please try again")

            elif x == 7:
                choice = int(input("Please select: \n    1. Sports & Gaming \n    2. Travels & Logistics "
                                   "\n    3. Data and PayTV \n    4. Distributor Payments "
                                   "\n    5. Search Biller \n    ---->: "))
                if choice:
                    print("The programme doesn't work from here, sorry")

            elif x == 8:
                choice = int(input("1.PIN \n2.Cardless \n3.Opt In \n4.Opt Out \n5.Loan Balance \n6.Generate Token"
                                   "\n7.Cheque Status \n8.Back \n9.Next \n --->: "))
                if choice:
                    print("The programme doesn't work from here, sorry")
            else:
                print("Invalid option entered, please try again")
        except ValueError:
            print("Invalid option entered, please try again")

    else:
        print("Invalid USSD code, please try again")


mock_ussd()
