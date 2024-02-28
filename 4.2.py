def splitting(string,delimiter):
    tokens=string.split(delimiter)
    for token in tokens:
        print(token)


def main():
    string1='"That\'s my house",he said'
    string2="one two\tthree\nfour five"
    string3="My name is\"Lucy\"."
    splitting(string1," ")
    print()
    splitting(string2,"\t")
    print()
    splitting(string2,"\n")
    print()
    splitting(string3,"\"")



main()