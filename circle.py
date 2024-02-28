def profile(a,b,c,d):
    w=a+"is the name of the student"
    x=b+"is age of the student"
    y=c+"is student's program"
    z=d
    return w,x,y,z


def main():
    name=input("Enter student's name: ")
    age=(input("Enter student's age: "))
    Degreeprogram=input("Enter student's degree program")
    Active=bool(input("Is the record still active? If no don't enter anything"))
    hello=profile(name,age,Degreeprogram,Active)
    print(hello)

main()

