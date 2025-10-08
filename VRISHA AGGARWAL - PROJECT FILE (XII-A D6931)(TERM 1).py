import random
import pickle

book=[]
binary_file="lbms.dat"

def option1():
    print("The function you have chosen is : Enter a new book - in the library management system")
    n=int(input("Enter the number of books you would like to add : "))
    for i in range(n):
         name = input("Enter the name of the book : ")
         author = input("Enter the author's name : ")
         genre= input("Enter the genre : ")
         identity_number = random.randint(1000, 9999)
         a=[name,author,genre,identity_number]
         book.append(a)
         with open(binary_file,"wb") as f:
             pickle.dump(book, f)

def option2():
    print("The function you have chosen is : Search a book and obtain its respective details")
    global book
    try:
        with open(binary_file,"rb") as f:
            a = pickle.load(f)
    except EOFError:
        book=[]
    s=int(input("Enter 1 - if you would like to search based on identity number and 2 - if you would like to search based on name : "))
    if s==1:
        b=int(input("Enter the respective identity number : "))
        for i in a:
            if i[3]==b:
                print(i)
    elif s==2:
        b=input("Enter the respective name of the book : ")
        for i in a:
            if i[0]==b:
                print(i)
    else:
        pass

def option3():
    print("The function you have chosen is : Update a book and its details")
    global book
    try:
        with open(binary_file,"rb") as f:
            a = pickle.load(f)
    except EOFError:
        book=[]
    b=int(input("Enter the respective identity number you would like to update : "))
    for i in a:
        if i[3]==b:
            print("The books' current details are :",i)
            c=input("Enter the updated books' name : ")
            d=input("Enter the updated author's name : ")
            e=input("Enter the updated genre of the book : ")
            print("The new identity number will be assigned according to the system")
            i[0]=c
            i[1]=d
            i[2]=e
            i[3]=random.randint(1000, 9999)
            print("The books' updated details are :",i)
            with open(binary_file,"wb") as f:
             pickle.dump(a, f)
        else:
            pass

def option4():
    print("The function you have chosen is : View all books and their details")
    global book
    try:
        with open(binary_file,"rb") as f:
            a = pickle.load(f)
    except EOFError:
        book=[]
    for i in a:
        print(i)

def option5():
    print("The function you have chosen is : View all authors the library offers")
    print("All the authors offered by the library are as follows : ")
    global book
    try:
        with open(binary_file,"rb") as f:
            a = pickle.load(f)
    except EOFError:
        book=[]
    for i in a:
        print(i[1])

def option6():
    print("The function you have chosen is : View all the genres offered")
    global book
    try:
        with open(binary_file,"rb") as f:
            a = pickle.load(f)
    except EOFError:
        book=[]
    for i in a:
        print(i[2])

def option7():
    print("The function you have chosen is : View the count of all the number of books offered")
    global book
    try:
        with open(binary_file,"rb") as f:
            a = pickle.load(f)
    except EOFError:
        book=[]
    length=len(a)
    print("The number books the library currently accomodates is ",length)

def option8():
    print("The function you have chosen is : Delete a particular books' detail")
    global book
    try:
        with open(binary_file,"rb") as f:
            a = pickle.load(f)
    except EOFError:
        book=[]
    b=int(input("Enter the respective identity number you would like to delete : "))
    for i in a:
        if i[3]==b:
            a.remove(i)
            print("Successfully deleted !")
            with open(binary_file, "wb") as f:
             pickle.dump(a,f)
        else:
            pass
    
while True:
    print("WELCOME TO THE LIBRARY MANAGEMENT SYSTEM")
    print("Choose option (1: Opening the library management system) and (2 : For closing the homepage)")
    ch=int(input("Enter your option : "))
    if ch==1:
        while True:
            print('''
LIBRARY MANAGEMENT SYSTEM
The functions you can opt are :
1. Enter a new book - in the library management system
2. Search a book and obtain its respective details
3. Update a book and its details
4. View all books and their details
5. View all authors the library offers
6. View all the genres offered
7. View the count of all the number of books offered
8. Delete a particular books' details
9. Exit the management system''')
            opt=int(input("Enter the function you want to opt : "))
            if opt==1:
                option1()
            elif opt==2:
                option2()
            elif opt==3:
                option3()
            elif opt==4:
                option4()
            elif opt==5:
                option5()
            elif opt==6:
                option6()
            elif opt==7:
                option7()
            elif opt==8:
                option8()
            elif opt==9:
                print("We will now close the library management system. We will rederict you to the homepage !")
                break
            else:
                print("This partocular choice is invalid")
    elif ch==2:
        print("Thank you for visiting the library management homepage")
        break
    else:
        print("Invalid Choice")


    
    
    
    
    
