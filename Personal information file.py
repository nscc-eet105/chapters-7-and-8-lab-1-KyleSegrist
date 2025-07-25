#Kyle Segrist
# Chapters 7 & 8 lab 1
# July 14 2025
import sys
import csv

READ=("R","r")
WRITE=("W","w")
def main():

    #open file
    filename = input('Enter the name of the file you would like to open: ')

    #process file
    task = input("Would you like to (r)ead from or(w)rite to the file?: ")

    #for task in TASKS:
    if task in READ:
        read_file(filename)
    elif task in WRITE:
        write_file(filename)
    else:
        input('Enter "r" or "w" to continue')

    #close file
    print('Thank you for using the program.')


def read_file(filename):
    try:
        with open(filename, 'r') as infile:
            for line in infile:
                # remove new line character
                line = line.replace("\n","")
                # display requested file
                print(line)
        infile.close()
    except IOError:
        print('An error has occurred trying to open the file:',filename)

def write_file(filename):
    personal_info = ('First name', 'Last name', 'Street address', 'City', 'State', 'Zip code')
    try:
        with (open(filename, 'w',newline="") as file):
            writer = csv.writer(file)
            #get information from the user
            for i in personal_info:
                personal_data = []
                data = (input(f"Please enter your {i}: "))
                personal_data.append(data)
                writer.writerow(personal_data)

    except IOError:
        print('An error has occurred trying to open the file:',filename)

main()