# All import scripts to be here:

import time

# Import scripts stop here

# First message to run
print("Welcome to DarrotOS 0.1.1 Entertainment")
print("(c) 2019 Yetroll Enterprises; CarroTech Industries; The coding Monkeys inc ")
print("Coded by Daniel P, Shaurya J and Malakai H")

# All functions go here:

#    No functions added yet

# Functions stop here

loop = 1
while loop == 1:
    userInput = input("Please input Entertainment command ").lower()
    if userInput == "/help":
        # Help for each command can be placed here
        print("Help info here")
    else:
        # Make sure all commands are lowercase
        if userInput == "/shutdown":
            exit()
        else:
            if userInput == "/games":
                print("Welcome to the games menu!")
                time.sleep(1)
                print("Use /gameshelp if you would like to see all the games. Use /stop to exit")
                gamesLoop = 1
                while gamesLoop == 1:
                    input("Please input games command")
                    if userInput == "/gameshelp":
                        # Place games help here
                        print("Games help")
                    else:
                        # The following area you can add new games

                        if userInput == "workinprogress":
                            print("WorkInProgress")
                        else:
                            if userInput == "workinprogress":
                                print("WorkInProgress")
                            else:
                                print("Invalid command")
            else:
                if userInput == "workinprogress":
                    print("WorkInProgress")
                else:
                    if userInput == "workinprogress":
                        print("WorkInProgress")
                    else:
                        if userInput == "workinprogress":
                            print("WorkInProgress")
                        else:
                            if userInput == "workinprogress":
                                print("WorkInProgress")
                            else:
                                if userInput == "workinprogress":
                                    print("WorkInProgress")
                                else:
                                    print("Invalid command")

