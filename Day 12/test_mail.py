# python | Day 12
# Student or Professor.
# At a certain school, student email addresses end with @student.college.edu,
# while professor email addresses end with @prof.college.edu.
# Write a program that first asks the user how many email addresses they will be entering,
# and then has the user enter those addresses.
# After all the email addresses are entered, the program should print out a message
# indicating exactly how many student and professor emails were entered.

def check_mail():
    """ A function to check the type of email entered.

    This function first asks the user to enter the number of emails they intend to enter(num_of_mails).
    Then, an empty list(email_list) is created. A for-loop is initiated, the for loop allows the user to enter
    the mails up to the num_of_mail then appends it to the email_list.
    Another for-loop is used to split the mails at '@', then the conditional statements check whether a mail is
    a student or a professor mail. For every student or professor mail, the variables a or b(initialized at 0) is
    increased by 1 respectively.

    After which their values will be printed.

    """

    a, b = 0, 0
    num_of_mails = int(input("How many emails do you want to enter: "))
    email_list = []
    
    for i in range(0, num_of_mails):
        email_list.append(str(input("Enter the email address: ")))

    for mail in email_list:
        x_mail = mail.split("@")
        if "student.college.edu" in x_mail:
            a += 1
        elif "prof.college.edu" in x_mail:
            b += 1

    print("You entered {} student mail(s) and {} professor mail(s).".format(a, b))


check_mail()
