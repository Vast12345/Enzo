
# While True function to print the menu, following it up with a user input that determines whether you inputted the right file name correctly. Afterwards, it creates the fie route into fd and returns it whilst also using a try and except function to make sure it doesnt crash if anything goes wrong.
def openFile():
    while True:
        try:
            print("\n", "=" * 30, "\n")
            print("*** AVERAGE SPAM CONFIDENCE ***")
            print("\n", "=" * 30, "\n")
            name = input("Input file name --->")
            if name != "mbox.txt" and name != "mbox-short.txt":
                print("\n", "=" * 30, "\n")
                print("Invalid: File must be either (mbox-short.txt/mbox.txt)")
                input()
                continue
            fd = f"/home/Exegol-160/Enzo/11- Archivos/{name}"
            return fd
        except Exception as e:
            print("Error opening file", e)
            
# List funciton that creates an empty list of which all the instances of the X-DSPAM-Confidence numbers will be put into. Using a try and except catch, it opens the file route which was returned in the previous function and searches and adds everything relating to the SPAM Confidence. Finally, it returns the list with every SPAM Confidence within it.
def list(filename):
    setSpam = []
    
    try:
        with open(filename, "r") as file:
            for line in file:
                if line.startswith("X-DSPAM-Confidence"):
                    setSpam.append(line.split()[1])
    except Exception as e:
        print("Error in opening the file: ",e)
        
    return setSpam

# Average function that grabs the list that was returned in the previous function and goes through every element and adding it into the varibale suma, Then it divides it by the length of the list and returns the average.
def promedio(list):
    suma = 0
    for i in range(len(list)):
        suma += float(list[i])
        
    suma /= len(list)
    return suma
    
    
    
# Finally, all the functions being used to create the menu.
file = openFile()
lista = list(file)
theAvergage = promedio(lista)
print(f"The average X-DSPAM-Confidence is {theAvergage}")


