# All import scripts to be here:
import uuid
import smtplib, ssl
import time
import datetime

# Import scripts stop here


# First message to run
print("Welcome to DarrotOS 0.1.1")
print("(c) 2019 Yetroll Enterprises; CarroTech Industries; The coding Monkeys inc ")
print("Coded by Daniel P, Shaurya J and Malakai H")


# All functions go here:

def my_random_string(string_length):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4())  # Convert UUID format to a Python string.
    random = random.upper()  # Make all characters uppercase.
    random = random.replace("-", "")  # Remove the UUID '-'.
    return random[0:string_length]  # Return the random string.


# Functions stop here
# Test commit

try:
    passFile = open(r"C:\Users\Daniel\PycharmProjects\Darrot-OS\Daniel_OS_pass.txt", "r")
    passwordCheck = "null"
except:
    print("The directory of the 'Assets' file was not detected.")
    time.sleep(2)
    exit()

with open(r"C:\Users\Daniel\PycharmProjects\Darrot-OS\Daniel_OS_pass.txt", "r") as f:
    data = f.readlines()

for line in data:
    infoList = line.split(";")

password = infoList[0]
FAemail = infoList[1]
FAstate = infoList[2]
name = infoList[3]
age = infoList[4]

# This script checks the time is 1st of April
currentDT = datetime.datetime.now()
if currentDT.strftime("%m") == "04" and currentDT.strftime("%d") == "01":
    print("Happy April Fools Day! (;")

# Resets all variables
unlockAttempt = 0
n1 = 0
n2 = 1
loggingIn = 1

# Checks for Password
while loggingIn == 1:
    userInput = input("Please enter the password ")
    if userInput == password:
        print("Password correct!")
        if infoList[2] == "true":
            print("2FA has been enabled.")
            FAcode = my_random_string(8)
            port = 465  # For SSL
            password = "5xPCPGIsBn6YN8sangyYY7bVB#QD#ahi3UYEF&zsAsKINH4rYxem61Mngmy#02@8"

            # Create a secure SSL context
            context = ssl.create_default_context()

            with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
                server.login("develeopmenttest1@gmail.com", password)

                import smtplib, ssl

            port = 465  # For SSL
            smtp_server = "smtp.gmail.com"
            sender_email = "develeopmenttest1@gmail.com"  # Enter your address

            message = """Subject: Your 2FA code

                        Thank you for enabling 2FA. Your 2FA code is {FA}""".format(FA=FAcode)

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, FAemail, message)
            print("An email has been sent to", FAemail)
            userInput = input("Please input the code below ")
            if userInput == FAcode:
                print("Access Granted!")
                passFile.close()
                loggingIn = 0
            else:
                print("Incorrect code")
        else:
            print("Access Granted!")
            passFile.close()
            loggingIn = 0
    else:
        print("Incorrect password, please try again")

n2 = 0
# The following loop looks at what command you type and reacts accordingly
while n2 == 0:
    commandInput = input("How may I help you today? ")
    if commandInput == "/help":
        # Put all the help for commands here
        print("Use /sysinfo to bring up information about the system!")
        print("Use /calculator to do basic addition problems!")
        print("Use /setpassword to change your password!")
        print("Use /shutdown to shutdown the terminal!")
        print("Use /setinfo to set your name and age!")
        print("Use /info to get your name and age!")
        print("Use /time to get the current time!")
        print("Use /date to get the current date!")
        print("Use /setPass to change your password!")
        print("Use /2FAconfig to enable or disable 2FA")
    else:
        if commandInput == "/calculator":
            try:
                n = 0
                k = 0
                operation = 0
                while n == 0:
                    k = 0
                    operation = 0
                    print("Welcome to the calculator! I support addition, subtraction, division and multiplication!")
                    input("Press enter to continue!")
                    while operation == 0:
                        print("Would you like for me to")
                        print("Add (a)")
                        print("Subtract (s)")
                        print("Multiply (m)")
                        inputAnswer = input("or Divide? (d)")
                        if inputAnswer == "a":
                            operation = "a"
                        else:
                            if inputAnswer == "s":
                                operation = "s"
                            else:
                                if inputAnswer == "m":
                                    operation = "m"
                                else:
                                    if inputAnswer == "d":
                                        operation = "d"
                                    else:
                                        print("Sorry! Please use either a, s, m or d")
                    firstNumber = int(input("What is your first number? "))
                    secondNumber = int(input("What is your second number? "))
                    if inputAnswer == "a":
                        answer = firstNumber + secondNumber
                    else:
                        if inputAnswer == "s":
                            answer = firstNumber - secondNumber
                        else:
                            if inputAnswer == "m":
                                answer = firstNumber * secondNumber
                            else:
                                if inputAnswer == "d":
                                    answer = firstNumber / secondNumber
                    print("Your answer was", answer)
                    while k == 0:
                        inputAnswer = input("Would you like to use the calculator again? [y / n] ")
                        if inputAnswer == "n":
                            n = 1
                            k = 1
                        else:
                            if inputAnswer == "y":
                                print("Sure thing!")
                                k = 1
                            else:
                                print("Please enter either y or n")
            except:
                print("It seems that an number that you have inputted has crashed the calculator. Please try again.")

        else:
            if commandInput == "/setPass":
                passwordCheck = input("Verify it's you by inputting the previous password ")
                if passwordCheck == password:
                    passFile.close()
                    passFile = open(r"C:\Users\Daniel\PycharmProjects\Darrot-OS\Daniel_OS_pass.txt", "w")
                    passwordCheck = input("What would you like to set the password to? ")
                    print("password successfully set to", passwordCheck)
                    infoList[0] = passwordCheck
                    convertedList = ';'.join(infoList)
                    passFile.write(convertedList)
                    passFile.close()
                    password = infoList[0]
                else:
                    print("Incorrect password entered")
            else:
                if commandInput == "/shutdown":
                    print("Shutting down")
                    time.sleep(1)
                    print(".")
                    time.sleep(1)
                    print("..")
                    time.sleep(1)
                    print("...")
                    time.sleep(1)
                    n2 = 1
                else:
                    if commandInput == "/setinfo":
                        # I need to implement this to make it write the info the the text file
                        passfile = open(r"C:\Users\Daniel\PycharmProjects\Darrot-OS\Daniel_OS_pass.txt", "w")
                        name = input("What is your name? ")
                        age = input("What is your age? ")
                        infoList[3] = name
                        infoList[4] = age
                        convertedList = ';'.join(infoList)
                        print(convertedList)
                        passFile.write(convertedList)
                        pass


                    else:
                        if commandInput == "/info":
                            if name == 0 and age == 0:
                                print("Info has not been set, to set your info please type /setinfo")
                            else:
                                print("Your name is", name)
                                print("You are", age, "years old")
                        else:
                            if commandInput == "/time":
                                # Fetches the time and formats it to display it
                                currentDT = datetime.datetime.now()
                                print("The current time is", (currentDT.strftime("%I:%M:%S %p")))
                            else:
                                if commandInput == "/date":
                                    # Fetches the date and formats it to display it
                                    currentDT = datetime.datetime.now()
                                    print("The current date is", (currentDT.strftime("%d/%m/%Y")))
                                else:
                                    if commandInput == "/changePass":
                                        oldPass = input("Please input old password ")
                                        if oldPass == password:
                                            password = input("Please input the new password")
                                            FAstate = "false"
                                            passFile.close()
                                            passFile = open(
                                                r"C:\Users\Daniel\PycharmProjects\Darrot-OS\Daniel_OS_pass.txt", "w")
                                            infoList[0] = password
                                            infoList[1] = FAemail
                                            infoList[2] = FAstate
                                            infoList[3] = name
                                            infoList[4] = age
                                            convertedList = ';'.join(infoList)
                                            passFile.write(convertedList)
                                            passFile.close()
                                        else:
                                            print("Sorry, incorrect password")
                                    else:
                                        if commandInput == "/2FAconfig":
                                            # You can enable or disable 2FA right here
                                            userInput = input(
                                                "Would you like to enable 2FA (/enable2FA) or disable 2FA (/disable2FA)? ")
                                            if userInput == "/enable2FA":
                                                passwordCheck = input(
                                                    "Verify it's you by inputting the previous password ")
                                                if passwordCheck == password:
                                                    FAemail = input("Please input your 2FA email ")
                                                    FAcode = my_random_string(8)
                                                    port = 465  # For SSL
                                                    password = "5xPCPGIsBn6YN8sangyYY7bVB#QD#ahi3UYEF&zsAsKINH4rYxem61Mngmy#02@8"

                                                    # Create a secure SSL context
                                                    context = ssl.create_default_context()

                                                    with smtplib.SMTP_SSL("smtp.gmail.com", port,
                                                                          context=context) as server:
                                                        server.login("develeopmenttest1@gmail.com", password)

                                                        import smtplib, ssl

                                                    port = 465  # For SSL
                                                    smtp_server = "smtp.gmail.com"
                                                    sender_email = "develeopmenttest1@gmail.com"  # Enter your address

                                                    message = """Subject: Your 2FA code

                                                                Thank you for enabling 2FA. Your 2FA code is {FA}""".format(
                                                        FA=FAcode)

                                                    context = ssl.create_default_context()
                                                    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                                                        server.login(sender_email, password)
                                                        server.sendmail(sender_email, FAemail, message)
                                                    print("An email has been sent to", FAemail)
                                                    userInput = input(
                                                        "We have sent you a 2FA code. Please input below ")

                                                    if FAcode == userInput:
                                                        FAstate = "true"
                                                        passFile.close()
                                                        passFile = open(
                                                            r"C:\Users\Daniel\PycharmProjects\Darrot-OS\Daniel_OS_pass.txt",
                                                            "w")
                                                        infoList[1] = FAemail
                                                        infoList[2] = FAstate
                                                        convertedList = ';'.join(infoList)
                                                        passFile.write(convertedList)
                                                        passFile.close()

                                                        print("Two Factor Authentication has been enabled with",
                                                              FAemail)
                                                    else:
                                                        print("Incorrect code inputted, please try again")


                                                else:
                                                    print("Incorrect password entered")

                                            else:
                                                if userInput == "/disable2FA":
                                                    passwordCheck = input(
                                                        "Verify it's you by inputting the previous password ")
                                                    if passwordCheck == password:
                                                        FAemail = input("Please input your 2FA email ")
                                                        FAcode = my_random_string(8)
                                                        port = 465  # For SSL
                                                        password = "5xPCPGIsBn6YN8sangyYY7bVB#QD#ahi3UYEF&zsAsKINH4rYxem61Mngmy#02@8"

                                                        # Create a secure SSL context
                                                        context = ssl.create_default_context()

                                                        with smtplib.SMTP_SSL("smtp.gmail.com", port,
                                                                              context=context) as server:
                                                            server.login("develeopmenttest1@gmail.com", password)

                                                            import smtplib, ssl

                                                        port = 465  # For SSL
                                                        smtp_server = "smtp.gmail.com"
                                                        sender_email = "develeopmenttest1@gmail.com"  # Enter your address

                                                        message = """Subject: Your 2FA code

                                                        Thank you for enabling 2FA. Your 2FA code is {FA}""".format(
                                                            FA=FAcode)

                                                        context = ssl.create_default_context()
                                                        with smtplib.SMTP_SSL(smtp_server, port,
                                                                              context=context) as server:
                                                            server.login(sender_email, password)
                                                            server.sendmail(sender_email, FAemail, message)
                                                        print("An email has been sent to", FAemail)
                                                        userInput = input(
                                                            "We have sent you a 2FA code. Please input below ")
                                                        if FAcode == userInput:
                                                            FAstate = "false"
                                                            passFile.close()
                                                            passFile = open(
                                                                r"C:\Users\Daniel\PycharmProjects\Darrot-OS\Daniel_OS_pass.txt",
                                                                "w")
                                                            infoList[1] = FAemail
                                                            infoList[2] = FAstate
                                                            convertedList = ';'.join(infoList)
                                                            passFile.write(convertedList)
                                                            passFile.close()

                                                            print("Two Factor Authentication has been disabled with",
                                                                  FAemail)
                                                        else:
                                                            print("Incorrect code inputted, please try again")
                                                    else:
                                                        print("Incorrect password entered")
                                                else:
                                                    print("Unknown command")
                                        else:
                                            if commandInput == "/sysinfo":
                                                print("DarrotOS 0.1.1 system information")
                                                print(
                                                    "(c) 2019 Yetroll Enterprises; CarroTech Industries; The Coding Monkeys inc ")
                                                print("Coded by Daniel P, Shaurya J and Malakai H")
                                                print("Root By Daniel P + Malakai H.")
                                                print(
                                                    "You can visit the github page for this project ---> https://github.com/daniel071/Darrot-OS")
                                                print("Coded on Python (Pycharm)")
                                                # More info can be added here
                                            else:
                                                if commandInput == "newCommandHere":
                                                    print(
                                                        "Work in progress (This is put here to prevent a syntax error")
                                                    # New command goes here
                                                else:
                                                    print("Unknown command")