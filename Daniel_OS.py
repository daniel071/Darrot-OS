# By Daniel Pavela 2019
# Copyright Daniel Pavela
import uuid
import smtplib, ssl

def my_random_string(string_length):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4()) # Convert UUID format to a Python string.
    random = random.upper() # Make all characters uppercase.
    random = random.replace("-","") # Remove the UUID '-'.
    return random[0:string_length] # Return the random string.

passFile = open(r"E:\Programming\Daniel_OS_pass.txt", "r")
import datetime
passwordCheck = "null"
import time

with open(r"E:\Programming\Daniel_OS_pass.txt", "r") as f:
    data = f.readlines()

for line in data:
    infoList = line.split(";")

password = infoList[0]
FAemail = infoList[1]
FAstate = infoList[2]
currentDT = datetime.datetime.now()
print(currentDT.strftime("%m"))
unlockAttempt = 0
n1 = 0
n2 = 1
name = 0
age = 0
loggingIn = 1
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

        else:
            if commandInput == "/setPass":
                passwordCheck = input("Verify it's you by inputting the previous password ")
                if passwordCheck == password:
                    passFile.close()
                    passFile = open(r"E:\Programming\Daniel_OS_pass.txt", "w")
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
                        name = input("What is your name? ")
                        age = input("What is your age? ")


                    else:
                        if commandInput == "/info":
                            if name == 0 and age == 0:
                                print("Info has not been set, to set your info please type /setinfo")
                            else:
                                print("Your name is", name)
                                print("You are", age, "years old")
                        else:
                            if commandInput == "/time":
                                currentDT = datetime.datetime.now()
                                print("The current time is", (currentDT.strftime("%I:%M:%S %p")))
                            else:
                                if commandInput == "/date":
                                    currentDT = datetime.datetime.now()
                                    print("The current date is", (currentDT.strftime("%d/%m/%Y")))
                                else:
                                    if commandInput == "/changePass":
                                        oldPass = input("Please input old password ")
                                        if oldPass == password:
                                            passFile = open(r"E:\Programming\Daniel_OS_pass.txt", "w")
                                            newPass = input("What would you like to change the password to? ")
                                            passFile.write(newPass)
                                            passFile.close()
                                        else:
                                            print("Sorry, incorrect password")
                                    else:
                                        if commandInput == "/2FAconfig":
                                            userInput = input("Would you like to enable 2FA (/enable2FA) or disable 2FA (/disable2FA)? ")
                                            if userInput == "/enable2FA":
                                                passwordCheck = input("Verify it's you by inputting the previous password ")
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
                                                                
                                                                Thank you for enabling 2FA. Your 2FA code is {FA}""".format(FA=FAcode)

                                                    context = ssl.create_default_context()
                                                    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                                                        server.login(sender_email, password)
                                                        server.sendmail(sender_email, FAemail, message)
                                                    print("An email has been sent to", FAemail)
                                                    userInput = input("We have sent you a 2FA code. Please input below ")

                                                    if FAcode == userInput:
                                                        FAstate = "true"
                                                        passFile.close()
                                                        passFile = open(r"E:\Programming\Daniel_OS_pass.txt", "w")
                                                        infoList[1] = FAemail
                                                        infoList[2] = FAstate
                                                        convertedList = ';'.join(infoList)
                                                        passFile.write(convertedList)
                                                        passFile.close()

                                                        print("Two Factor Authentication has been enabled with", FAemail)
                                                    else:
                                                        print("Incorrect code inputted, please try again")


                                                else:
                                                    print("Incorrect password entered")

                                            else:
                                                if userInput == "/disable2FA":
                                                    passwordCheck = input("Verify it's you by inputting the previous password ")
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
                                                        
                                                        Thank you for enabling 2FA. Your 2FA code is {FA}""".format(FA=FAcode)

                                                        context = ssl.create_default_context()
                                                        with smtplib.SMTP_SSL(smtp_server, port,
                                                                              context=context) as server:
                                                            server.login(sender_email, password)
                                                            server.sendmail(sender_email, FAemail, message)
                                                        print("An email has been sent to", FAemail)
                                                        userInput = input("We have sent you a 2FA code. Please input below ")
                                                        if FAcode == userInput:
                                                            FAstate = "false"
                                                            passFile.close()
                                                            passFile = open(r"E:\Programming\Daniel_OS_pass.txt", "w")
                                                            infoList[1] = FAemail
                                                            infoList[2] = FAstate
                                                            convertedList = ';'.join(infoList)
                                                            passFile.write(convertedList)
                                                            passFile.close()

                                                            print("Two Factor Authentication has been disabled with",FAemail)
                                                        else:
                                                            print("Incorrect code inputted, please try again")
                                                    else:
                                                        print("Incorrect password entered")
                                                else:
                                                    print("Unknown command")
                                        else:
                                            print("Unknown command")