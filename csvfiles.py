import csv



def readcsv(name):
    try:
        with open(name,'r') as file:
            read=csv.reader(file) 
            next(read) #skips the header using the function next
            for line in read:
                print(line) 

    except FileNotFoundError:
        print("Unable to find file")



def main():
    name=input("File name:")
    readcsv(name)


main()