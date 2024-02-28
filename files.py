def files(name):
    try:
        with open(name,"r") as file:
            name1=input("enter the word")
            linenum=1
            for line in file:
                if name1 in line:
                    print("word found in line number",linenum)

                else:
                    print("Word not found",linenum)
            linenum=linenum+1

    except FileNotFoundError:
        print("Your file is not there")

    except:
        print("ERROR")








#for i in range(size):
#print(line[i])



def main():
    filename=input("enter file name w file path")
    files(filename)


if __name__=="__main__":
    main()