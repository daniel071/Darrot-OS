# By Daniel Pavela 2019


aToZ = [["a", 1], ["b", 2], ["c", 3], ["d", 4], ["e", 5], ["f", 6], ["g", 7], ["h", 8], ["i", 9], ["j", 10], ["k", 11],
        ["l", 12], ["m", 13], ["n", 14], ["o", 15], ["p", 16], ["q", 17], ["r", 18], ["s", 19], ["t", 20], ["u", 21],
        ["v", 22], ["w", 23], ["x", 24], ["y", 25], ["z", 26]]

n1 = 1
idCheck = 0
# Lists start at 0 like how a big boi starts


def calculate_value(firstname):
    global aToZ
    global valuelist
    global namevalue

    namevalue = 0
    a_to_z_loop = 1
    letterid = 0
    alphaid = 0
    lastvar = 0
    lastvarloop = 1

    while lastvarloop == 1:
        try:
            firstname[letterid]
            letterid = letterid + 1
        except:
            lastvar = letterid
            letterid = 0
            lastvarloop = 0

    while letterid < lastvar:
        while a_to_z_loop == 1:
            if firstname[letterid] == aToZ[alphaid][0]:
                namevalue = namevalue + aToZ[alphaid][1]
                a_to_z_loop = 0
            else:
                alphaid = alphaid + 1
        alphaid = 0
        letterid = letterid + 1
        a_to_z_loop = 1

    return namevalue


def name_game():
    print("Would like to do single or multi? [s / m]")
    userInput = input("")
    if userInput == "s":
        print("What is your first name")
        firstName = input("").lower()
        print(calculate_value(firstName))

    elif userInput == "m":
        print("What is the first name")
        firstName = input("").lower()
        valueOne = calculate_value(firstName)

        print("What is your second name")
        secondName = input("").lower()
        valueTwo = calculate_value(secondName)

        finalValue = (valueOne + valueTwo) / 2
        print("Your score was", finalValue)