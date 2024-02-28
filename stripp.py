def lines(line1):
    try:
        with open("Filewriting.txt",'w') as file:
        
            while line1:
                file.write(line1+'\n')
                line1=input("enter a new line")

    except IOError:
        print("Error")

def linesread():
    with open("Filewriting.txt",'r') as file:
        for line in file:
            print(line)



def main():
    line1=input("enter a line")
    lines(line1)
    linesread()

main()