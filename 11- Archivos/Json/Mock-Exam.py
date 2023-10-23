import json

def readNum(num):
    while True:
        try:
            n = int(input(num))
            if n < 1:
                print("Error: Invalid input, must be a positive integer")
                input("Press any key to continue ... ")
                print("\n", "=" * 30, "\n")
                continue
            return n
        except ValueError:
            print("Error: Invalid input, must be an integer")
            input("Press any key to continue ... ")
            print("\n", "=" * 30, "\n")

def readTitle(msj):
    while True:
        try:
            phrase = input(msj)
            phrase = phrase.strip()
            if len(phrase) == 0 or phrase.isdigit() == True:
                print("Error: Invalid input, must be a string")
                input("Press any key to continue ... ")
                print("\n", "=" * 30, "\n")
                continue
            return phrase
        except Exception as e:
            print(f"Error: Invalid input, must be a string\n{e}")
            input("Press any key to continue ... ")
            print("\n", "=" * 30, "\n")

def MainMenu():
    while True:
        try:
            print("\n")
            print("*** Bank ***".center(40))
            print("CHOOSE OPTION".center(40))
            print("\n", "=" * 38, "\n")
            print("1- Information regarding cards")
            print("2- Information regarding users")
            print("3- Exit\n")
            n = int(input("Choose an option (1-3) ---> "))
            if n < 1 or n > 3:
                print("Invalid: Choose between 1-3")
                print("\n", "=" * 30, "\n")
                input("Press any key to continue ... ")()
                continue
            return n
        except ValueError:
            print("Invalid: Input must be an integer between 1-3")
            print("\n", "=" * 30, "\n")
            input()

def menuCards():
    while True:
        try:
            print("\n")
            print("*** INFO CARDS ****")
            print("1- Add Card")
            print("2- Modify Card")
            print("3- Delete Card")
            print("4- New Report")
            print("5- Remove Report")
            print("6- Exit")
            n = readNum("Input which option you would like to select")
            if n < 1 or n > 6:
                print("Invalid: Choose between 1-6")
                input("Press any key to continue ... ")()
                continue
            return n
        except ValueError:
            print("Invalid: Input must be an integer between 1-6")

def menuList():
    while True:
        try:
            print("\n")
            print("*** INFO LIST ***")
            print("1- Cards of one client")
            print("2- Information of Card")
            print("3- List Cards")
            print("4- List Customers")
            print("5- Amount of Card Types")
            print("6- Exit")
            n = readNum("Input a number (1-3) --> ")
            if n > 6:
                print("Invalid: Input must be between 1-3")
                continue
            return n
        except ValueError:
            print("Error: Input must be an integer between 1-3")
            input("Press any key to continue ... ")()


def menuType():
    while True:
        try:
            type = ("Visa", "MasterCard", "American Express")
            print("\n\n Menu TYPE")
            print("1. Visa")
            print("2. MasterCard")
            print("3. American Express")
            n = readNum("Input which type is your card --> ")
            if n > 3:
                print("Invalid: Choose between 1-3")
                input("Press any key to continue ... ")()
            return type[n - 1]
            
        except ValueError:
            print("Error: Input an integer between 1-3")

def Expiration():
    while True:
        try:
            months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
            m = readNum("Choose which month for expiration (1-12) --> ")
            if m > 12:
                print("Invald, month must be between 1-12")
                continue
            return months[m - 1]
        except ValueError:
            print("Invalid: Input an integer between 1-12")

def editMenu():
    while True:
        print("*** Modify Book ***".center(45))
        print("1- Edit cedula")
        print("2- Edit CardType")
        print("3- Edit Expiration date")
        print("4- Edit Name")
        print("5- Exit")
        n = int(input("Choose which option you would like to modify: "))
        if n < 1 or n > 5:
            print("Error: Input must be between 1 and 5")
            input("Press any key to continue ... ")
            print("\n", "=" * 30, "\n")
            continue
        elif n == 5:
            break
        return n



def addCard(datacards, route):
    print("\n\n 1. Add Card")
    ced = readNum("Input cedula --> ")
    customer = findCustomer(datacards, ced)

    if customer is not None:


        cardReport = []
        cardNum = readNum("Input Number for card --> ")
        cardType = menuType()
        cardExp = Expiration()
        cardName = readTitle("Input your name --> ")
        cardReport.append(readNum("Input your report --> "))


        card_data = {"cardNumber":cardNum,
                     "cardType":cardType,
                     "cardExp":cardExp,
                     "cardName":cardName,
                     "cardReport":cardReport
        }
        customer["cards"].append(card_data)

    else:
        cardReport = []
        cardNum = readNum("Input Number for card --> ")
        cardType = menuType()
        cardExp = Expiration()
        cardName = readTitle("Input your name --> ")
        cardReport.append(readNum("Input your report --> "))

        new_customer = {
            "cedula":ced,
            "cards": [{
                "cardNumber":cardNum,
                "cardType":cardType,
                "cardExp":cardExp,
                "cardName":cardName,
                "cardReport":cardReport
            }]
        }
        datacards.append(new_customer)

        if saveCard(datacards, route) == True:
            input("The card has been registered successfully.\nPress any key to continue ... ")
        else:
            input("An error occurred while registering the card.")


def existId(card, datacards):
    for data in datacards:
        k = int(list(data.keys())[0])
        if k == card:
            return True
    return False

def saveCard(datacards, route):
    try:
        with open(route, "w") as fd:
            try:
                json.dump(datacards, fd)
                return True
            except Exception as e:
                print("Error in opening archive to save card.\n", e)
                return None

    except Exception as e:
        print("Error in saving the information of the new register.\n")
        return None

def modifyCard(datacards, route):
    ced = readNum("Input cedula --> ")
    customer = findCustomer(datacards, ced)

    if customer is not None:
        for i, card in enumerate(customer["cards"], start=1):
            print(f"{i}. Card Number: {card['cardNumber']}, Card Type: {card['cardType']}, Card Name: {card['cardName']}")

        card_index = readNum("Select the card you wish to modify: ")
        if 1 <= card_index <= len(customer["cards"]):
            card_to_modify = customer["cards"][card_index - 1]
            n = editMenu()
            if n == 1:
                card_to_modify["cardNumber"] = readNum("Input new card number --> ")
            elif n == 2:
                card_to_modify["cardType"] = menuType()
            elif n == 3:
                card_to_modify["cardExp"] = Expiration()
            elif n == 4:
                card_to_modify["cardName"] = readTitle("Input new name --> ")
            else:
                print("Invalid option")
                return

            if saveCard(datacards, route) == True:
                print("The card has been modified successfully")
                input("Press any key to continue ... ")
            else:
                print("An error occurred modifying the card.")
        else:
            print("Invalid card selection")
    else:
        print("Customer not found")

def deleteCard(datacards, route):
    print("\n\n3. DELETE CARD")

    card = readNum("Input the card number -- > ")
    if not existId(card, datacards):
        print("That card does not exist")
        input("Press any key to continue ... ")
        return

    for i in range(len(datacards)):
        data = datacards[i]
        k = int(list(data.keys())[0])
        if k == card:
            del datacards[i]
            break
    if saveCard(datacards, route) == True:
        print("The card was erased successfully")
        input("Press any key to continue ... ")
    else:
        print("An error occurred deleting the card.")

def newReport(datacards, route):
    print("\n\n3. NEW REPORT")

    card = readNum("Input the card number -- > ")
    if not existId(card, datacards):
        print("That card does not exist")
        input("Press any key to continue ... ")
        return

    for i in range(len(datacards)):
        data = datacards[i]
        k = int(list(data.keys())[0])
        if k == card:
            datacards[i][str(card)]["cardReport"].append(readNum("Input new report"))

    if saveCard(datacards, route) == True:
        print("The report was successfully saved")
        input("Press any key to continue ... ")
    else:
        print("An error occurred saving the report.")

def delReport(datacards, route):
    print("\n\n3. DELETE REPORT")

    card = readNum("Input the card number -- > ")
    if not existId(card, datacards):
        print("That card does not exist")
        input("Press any key to continue ... ")
        return

    for i in range(len(datacards)):
        data = datacards[i]
        k = int(list(data.keys())[0])
        if k == card:
            lstRep = datacards[i][str(card)]['cardReport']
            if len(lstRep) == 0:
                print("Card does not have any reports")
            else:
                print("Reports for this card:")
                for j, report in enumerate(lstRep):
                    print(f"{j+1}. {report}")

                report_index = readNum("Enter the index of the report you want to delete: ")

                if report_index <= len(lstRep):
                    deleted_report = lstRep.pop(report_index - 1)
                    print(f"Report '{deleted_report}' has been deleted.")
                    datacards[i][str(card)]['cardReport'] = lstRep
                else:
                    print("Invalid index. Report not deleted.")
                break

    if saveCard(datacards, route) == True:
        print("The report was removed successfully.")
        input("Press any key to continue ... ")
    else:
        print("An error occurred removing the report.")

def findCustomer(datacards, ced):
    for customer in datacards:
        if customer["cedula"] == ced:
            return customer
        return None

def listCards(datacards, ced):
    customer = findCustomer(datacards, ced)
    if customer:
        print(f"Customer Cedula: {customer['cedula']}")
        print("List of Cards:")
        for i, card in enumerate(customer.get("cards", []), start=1):
            print(f"{i}. Card Number: {card.get('cardNumber')}")
            print(f"   Card Type: {card.get('cardType')}")
            print(f"   Card Name: {card.get('cardName')}")
            # Add more card details as needed
    else:
        print("Customer not found.")

def clientCards(datacards, route):
    for customer in datacards:
        print(f"Cedula: {customer['cedula']}")
        for i, card in enumerate(customer['cards'], start=1):
            print(f"{i}. Card Number: {card['cardNumber']}, Card Type: {card['cardType']}, Card Expriration Date: {card['cardExp']}, Card Name: {card['cardName']} ")
            print("\n", "=" * 30, "\n")
            input("Press any key to continue ... ")


def searchCard(datacards, route):
    print("\n\n2. SEARCH CARD")
    card_number_to_find = readNum("Enter the card number you wish to find --> ")
    found_card = findCardbyNumber(datacards, card_number_to_find)
    if found_card:
        print(f"CARD INFORMATION:\nCard Number: {card_number_to_find}\nCard Type: {found_card.get('cardType')}\nCard Expiration Date: {found_card.get('cardExp')}\nCard Name: {found_card.get('cardName')}")
    else:
        print("Card not found")

def findCardbyNumber(datacards, cardNumber):
    for customer in datacards:
        for card in customer.get("cards", []):
            if card.get("cardNumber") == cardNumber:
                return card
    return None

def listCustomers(datacards):
    print("\nListing customers...")
    for customer in datacards:
        print(f"Cedula: {customer['cedula']}")
        for card in customer['cards']:
            print(f"Card Name: {card['cardName']}")
            print("\n", "=" * 30, "\n")
            input("Press any key to continue ... ")


def findCustomer(datacards, ced):
    for customer in datacards:
        if customer["cedula"] == ced:
            return customer
        return None
    
def listCardType(Data):
    print("CANTIDAD DE TARJETAS REGISTRADAS")
    Visa = 0
    American = 0
    Master = 0

    for customer in Data:
        for card in customer["cards"]:
            cardType = card["cardType"]
            if cardType == "Visa":
                Visa += 1
            elif cardType == "American Express":
                American += 1
            elif cardType == "MasterCard":
                Master += 1 

    print(f"Visa: {Visa}")
    print(f"American Express: {American}")
    print(f"MasterCard: {Master}")



def updateData(datacards, route):
    try:
        with open(route, "r") as fd:
            datacards = json.load(fd)
            print(datacards)
    except Exception as e:
        print("Error in trying to open or load the archive\n", e)

    return datacards

DataCards = []
RTCards = "Information-Cards.json"
DataCards = updateData(DataCards, RTCards)


while True:
    op = MainMenu()
    if op == 1:
        while True:
            option = menuCards()
            if option == 1:
                addCard(DataCards, RTCards)
            elif option == 2:
                modifyCard(DataCards, RTCards)
            elif option == 3:
                deleteCard(DataCards, RTCards)
            elif option == 4:
                newReport(DataCards, RTCards)
            elif option == 5:
                delReport(DataCards, RTCards)
            elif option == 6:
                break
    elif op == 2:
        while True:
            option = menuList()
            if option == 1:
                listCards(DataCards, RTCards)
            elif option == 2:
                searchCard(DataCards, RTCards)
                input("Press any key to continue ... ")
            elif option == 3:
                clientCards(DataCards, readNum("Enter the cedula of the cards you wish to search --> "))
                input("Press any key to continue ... ")
            elif option == 4:
                listCustomers(DataCards)
            elif option == 5:
                listCardType(DataCards)
                input("Press any key to continue ... ")
            elif option == 6:
                input("Press any key to continue ... ")
                break
    elif op == 3:
        input("Press any key to continue ... ")
        break