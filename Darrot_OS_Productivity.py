# All import scripts to be here:

import time
import webbrowser

# Import scripts stop here

# First message to run
print("Welcome to DarrotOS 0.1.1 Productivity")
print("(c) 2019 Yetroll Enterprises; CarroTech Industries; The coding Monkeys inc ")
print("Coded by Daniel P, Shaurya J and Malakai H")

# All functions go here:

#    No functions added yet

# Functions stop here


loop = 1
while loop == 1:
    userInput = input("Please input Productivity command ").lower()
    print(userInput)
    if userInput == "/help":
        # Help for each command can be placed here
        print("Redirecting you to the wiki page")
        time.sleep(1)
        webbrowser.open('https://github.com/daniel071/Darrot-OS/wiki/Productivity-terminal')

    else:
        # Make sure all commands are lowercase
        if userInput == "/shutdown":
            exit()
        else:
            if userInput == "/substitutetxt":
                print("Hello! I will substitute words into different words in text documents!")
                try:
                    substituteDirectory = input("Please input the file directory of the document ")
                    substituteFile = open(substituteDirectory, "r")
                except:
                    print("Please input the correct directory!")
                    time.sleep(2)
                    exit()

                textFile = substituteFile.read()
                str(textFile)
                substituteFile.close()
                wordToSub = input("Which word do you want to substitute? ")
                wordToReplaceWith = input("Which word do you want to substitute to? ")
                newFile = textFile.replace(wordToSub, wordToReplaceWith)
                substituteFile = open(substituteFile, "w")
                substituteFile.write(newFile)
                substituteFile.close()
                print("Substituted", wordToSub, "with", wordToReplaceWith, "successfully!")
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

