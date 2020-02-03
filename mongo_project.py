import pymongo
import os

MONGODB_URI = ("mongodb+srv://myRoot:XXXXXXXXX@myamazingcluster-96wib.mongodb.net/XXXXXXX?retryWrites=true&w=majority")
DBS_NAME = "XXXXX"
COLLECTION_NAME = "XXXXXXX"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn

    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: {}").format(e)


def show_menu():
    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")

    option = input("Enter option: ")
    return option

def get_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")

    try:
        doc = coll.find_one({'first': first.lower(), 'last': last.lower()})
        print(doc)
    except:
        print("Error accessing the database")

    if not doc:
        print("")
        print("Error! No results found.")

    return doc

def add_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    dob = input("Enter dob > ")
    gender = input("Enter gender > ")
    hair_colour = input("Enter hair_coloure > ")
    occupation = input("Enter occupation > ")
    nationality = input("Enter nationality > ")

    new_doc = {'first': first.lower(), 'last': last.lower(), 'dob': dob, 'gender': gender.lower(),
           'hair_colour': hair_colour.lower(), 'occupations': occupation.lower(),
           'nationality': nationality.lower()}

    try:
        coll.insert(new_doc)
        print("")
        print("Document inserted")

    except:
        print("Error accessing the database")




def main_loop():
    while True:
        option = show_menu()
        if option == "1":
           add_record()
        elif option == "2":
            get_record()
        elif option == "3":
            print("You have selected option 3")
        elif option == "4":
            print("You have selected option 4")
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
            print("")


conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

main_loop()

