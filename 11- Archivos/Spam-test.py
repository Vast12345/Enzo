
# A try and except just in case there is some error with trying to access the archive
try:
    fd = open("11- Archivos/mbox.txt", "r")
    fd2 = open("11- Archivos/mbox-short.txt", "r")
except Exception as e:
    print("Error in trying to open archive")
    input()
# Empty lists that will contain every Spam confidence mentioned in the .txt files
setSpam = []
lstSpam = []

#grabs every element that is displayed right after the term X-DSPAM-Confidence and adds it to its respective list
for line in fd:
    if line.startswith("X-DSPAM-Confidence"):
        setSpam.append(line.split()[1])


for line in fd2:
    if line.startswith("X-DSPAM-Confidence"):
        lstSpam.append(line.split()[1])

# Close the files since we no longer need them
fd2.close()
fd.close()


# Empty variables that will hold the sum for each .txt file
suma = 0
sumaShort = 0

# The for loop that will grab every element within their respective list and continue adding up until the for loop is over
for i in range(len(setSpam)):
    suma += float(setSpam[i])

for i in range(len(lstSpam)):
    sumaShort += float(lstSpam[i])


# The input that allows you to only try to access mbox.txt and mbox-short.txt
while True:
    print("\n", "=" * 30, "\n")
    print("*** AVERAGE SPAM CONFIDENCE ***")
    print("\n", "=" * 30, "\n")
    file = input("Enter file name ---> ")
    if file == "mbox.txt":
        print(f"Average Spam confidence: {suma / len(setSpam)}")
        print("\n", "=" * 30, "\n")
        break  # To find the average I simply divided the sum with the length of the list
    elif file == "mbox-short.txt":
        print(f"Average Spam confidence: {sumaShort / len(lstSpam)}")
        print("\n", "=" * 30, "\n")
        break
    else:
        print("Invalid, file must be either: (mbox.txt) or (mbox-short.txt)")


