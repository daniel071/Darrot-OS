print("Welcome to CarrotOS 0.1.1")
print("(c) 2019 Yetroll Enterprises; CarroTech Industries ")
print("Coded by Daniel P, Shaurya J and Malakai H")
# By Daniel Pavela, Shaurya J and Malakai H 2019
access = 0
ips = 0
f = open(r"pswrd.txt","r")
if f.mode == "r":
    contents = f.read()
name1 = open(r"name.txt","r")
if name1.mode == "r":
    name = name1.read()
age1 = open(r"age.txt","r")
if age1.mode == "r":
    age = age1.read()
email1 = open(r"email.txt","r")
if email1.mode == "r":
    email = email1.read()
hunterii = open(r"hunter2installed.txt","r")
if hunterii.mode == "r":
    Hunter2 = hunterii.read()
while access == 0:
    upa = input("Enter Password:")
    if upa == contents:
        print("Password Correct.")
        access = 1
    else:
        if ips > 4:
            exit()
        ips = ips + 1
        print("Password Incorrect. ",ips, "attempts so far." )
while access == 1:
    commandInput = input("Input Commands here: ")
    if commandInput == "!meh":
        print(":|")
    if commandInput == "!happy":
        print(":)")
    if commandInput == "!sad":
        print(":(")
    if commandInput == "!help":
        print("Use !Calc to do basic Mathematics problems ")
        print("Use !shutdown to shutdown the terminal.")
        print("Use !TheHunterDX to play The Hunter Deluxe.")
        if Hunter2 == "true":
            print("Use !HunterII to play The Hunter 2")
        if Hunter2 == "false":
            print("Install The Hunter 2 By beating The Hunter DX!")
        print("Use !TextwriterPro to execute TextwriterPro 0.1.1")
        print("Use !Morehelp fore more help options")
    if commandInput == "!Morehelp":
        print("Use !info to get your name, age and email.")
        print("Use !date to get the current date/time.")
        print("Use !count to print all numbers from 0 to your choice.")
        print("Use !config to open Configuration Settings. (!configinfo for more")
    if commandInput == "!count":
        counting = 0
        endcount = input("The program will count to :")
        if int(endcount) >= 500000:
            print("The number is too large!")
        else:
            while counting <= int(endcount):
                print(counting)
                counting = counting + 1
    if commandInput == "!date":
        import datetime
        now = datetime.datetime.now()
        print("Current date and time: ")
        print(now.strftime("%Y-%m-%d %H:%M:%S"))
    if commandInput == "!configinfo":
        print("ALL OF THESE ONLY WORK IN CONFIG")
        print("Use !setpassword to change the password")
        print("Use !setinfo to change your info")
        print("Use !2FA to see the 2FA settings")
        print("Use !secretcommands to see secret commands")
    if commandInput == "!TextwriterPro":
        rorw = input("Read or Write?")
        if rorw == ("Write"):
            textwriter = input("Enter Text:")
            TextFile = open(r"Txtwrter.txt", "w")
            TextFile.write(textwriter)
            TextFile.close()
            print("File Saved.")
        else:
            if rorw == ("Read"):
                readtext1 = open(r"Txtwrter.txt","r")
                if readtext1.mode == "r":
                    readtext = readtext1.read()
                print(readtext)
                input("Press enter to close.")
    if commandInput == "!TheHunterDX":
        answer1 = 2
        answer2 = 2
        answer3 = 2
        answer4 = 2
        answer5 = 2
        answer6 = 2
        answer7 = 2
        print("T H E")
        print("|_| | | |\| -- |- |}")
        print("| | |-| | | |  |- |.")
        print("                 DX")
        print("(c) Yetroll Entertainment 2019")
        print("Use either z or x to control.")
        input("Press <-| Enter to begin your quest for survival.")
        print("You are in the jungle. A person")
        print("called John Murray is hunting you.")
        print("There is a split pathway. where do")
        gameanswer = input("you go?")
        if gameanswer == "z":
            answer1 = 1
        else:
            answer1 = 0
            if answer1 == "1":
                print("You turn right.")
                print("Stupid move. he's there.")
                print("You Die. Game Over")
                input("Press enter to continue.")
            if answer1 == 0:
                print("You turn left. You hear a")
                print("scream followed by a groan")
                print("do you jump(z) or go back?(x)")
                gameanswer = input("")
                if gameanswer == "z":
                    print("You jump down the gap.")
                    print("A thud is heard.")
                    print("You lose.")
                    input("Game over. Press enter to continue")
                else:
                    print("You turn back. To be greeted by John Murray")
                    gameanswer = input("Fight(z) or run(x)?")
                    if gameanswer == 'x':
                        print("you run.")
                        print("you trip.")
                        print("John kills you.")
                        print("Game over.")
                        input("Press enter to continue.")
                    if gameanswer == "z":
                        print("You fight a glorious fight")
                        print("You stab him in the neck and run")
                        print("You win...")
                        gameanswer = input("Game over. Do you want 'The Hunter II' for $11? Y/N")
                        if gameanswer == "Y":
                           if Hunter2 == "true":
                                print("The Hunter 2 Is already Installed!")
                        else:
                            print('Sorry! Our servers seem to be offline!')
                        if gameanswer == "N":
                            print("Exiting The Hunter DX...")
                        if gameanswer == "Freebie123":
                            if Hunter2 == "true":
                                print("The Hunter 2 Is already Installed!")
                            else:
                                print("Verification Code activated. Installing")
                                print("The Hunter II.")
                                Huntertwo = open(r"hunter2installed.txt", "w")
                                Huntertwo.write("true")
                                Huntertwo.close()
                                hunterii = open(r"hunter2installed.txt", "r")
                                if hunterii.mode == "r":
                                    Hunter2 = hunterii.read()
                                print("Installation complete. see !help")
                                print("to execute the game.")
                                input("Press enter to continue.")
                        else:
                            print("Exiting The Hunter DX")
    if commandInput == "!HunterII":
        if Hunter2 == "false":
            print("")
        if Hunter2 == "true":
            answer1 = 2
            answer2 = 2
            answer3 = 2
            answer4 = 2
            answer5 = 2
            answer6 = 2
            answer7 = 2
            print("T H E")
            print("| | | | |\| -- |- |} 2")
            print("|-| |-| | | |  |- |.")
            print("REVENGE OF THE MURRAY")
            print("(c) Yetroll Entertainment 2019")
            print("Use either z or x to control.")
            input("Press <-| Enter to begin your quest for survival.")
            print("You are in the desert. A family")
            print("called the Murray's are hunting you.")
            print("There is a split pathway. where do")
            gameanswer = input("you go?")
            if gameanswer == "z":
                answer1 = 1
            else:
                answer1 = 0
            if answer1 == "1":
                print("You turn right.")
                print("Stupid move. The mother's there.")
                print("You Die. Game Over")
                input("Press enter to continue.")
            if answer1 == 0:
                print("You turn left. You hear a")
                print("scream followed by a groan")
                print("do you jump(z) or go back?(x)")
                gameanswer = input("")
                if gameanswer == "z":
                    print("You jump down the gap.")
                    print("A thud is heard.")
                    print("You lose.")
                    input("Game over. Press enter to continue")
                else:
                    print("You turn back. To be greeted by John Murray")
                    gameanswer = input("Fight(z) or run(x)?")
                    if gameanswer == 'x':
                        print("you run.")
                        print("you trip.")
                        print("The father kills you.")
                        print("Game over.")
                        input("Press enter to continue.")
                    if gameanswer == "z":
                        print("You fight a glorious fight")
                        print("You stab all of them in the neck and run")
                        print("You win...")
                        print("Exiting The Hunter II...")
    if commandInput == "!shutdown":
        print("Shutdown System? Y/N")
        sds = input("")
        if sds == ("Y"):
            exit()
    if commandInput == "!Info":
        print("Name :", name)
        print("Age :", age)
        print("Email :", email)
    if commandInput == "!config":
        print("CarrotOS 0.1.1 Configuration Settings: Input Command Below")
        settingsfunc = input("")
        if settingsfunc == input("!sysinfo"):
            print("CarrotOS 0.1.1 system information")
            print("(c) 2019 Yetroll Enterprises; CarroTech Industries ")
            print("Coded by Daniel P, Shaurya J and Malakai H")
            print("Root By Malakai H.")
            print("Coded on Python (Pycharm)")
        if settingsfunc == "!secretcommands":
            print("Secret commands...")
            print("ONLY ACTIVATED BY MAIN TERMINAL.")
            print("THESE COMMANDS DO NOT WORK IN CONFIG")
            print("Use !meh to show 'meh' face.")
            print("Use !sad to show 'sad' face.")
            print("Use !happy to show 'happy' face.")
        if settingsfunc == "!setinfo":
            newname = input("New Name:")
            passFile = open(r"name.txt", "w")
            passFile.write(newname)
            print("Name saved as", newname)
            passFile.close()
            newage = input("New Age:")
            passFile = open(r"age.txt", "w")
            passFile.write(newage)
            print("Age saved as", newage)
            passFile.close()
            newemail = input("New Email:")
            passFile = open(r"email.txt", "w")
            passFile.write(newemail)
            print("Email saved as", newemail)
            passFile.close()
        if settingsfunc == "!setpassword":
            psreset = input("Input old password: ")
            if psreset == (contents):
                    newpsrd = input("Enter New Password: ")
                    passFile = open(r"pswrd.txt", "w")
                    passFile.write(newpsrd)
                    passFile.close()
                    print("Password Saved.")
    if commandInput == "!Calc":
        print("Welcome to the addition, subtraction, division and multiplication calculator")
        print("Root by Daniel P")
        input("Press enter to continue!")
        print("Enter the operation you want.")
        print("Add (a)")
        print("Subtract (s)")
        print("Multiply (m)")
        print("Divide (d)")
        inputAnswer = input("Input Choice:")
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
                        print("Please use either a, s, m or d")
            firstNumber = int(input("Input first number."))
            secondNumber = int(input("Input second number."))
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
                                if secondNumber == 0:
                                    print("Cannot Divide By 0!")
                                else:
                                    answer = firstNumber / secondNumber
        print("Your answer is", answer)
    else:
        print("")
