import sys
from proto.compiled import addressbook_pb2

def AskForAddress(person):
    person.id = int(input('Enter person ID: '))
    person.name = input('Enter name ID: ')

    email = input("Enter email address: ")
    if email != '':
        person.email = email
    while True:
        number = input('Enter phone number')
        if number == '':
            break

        phone_number = person.phones.add()
        phone_number.number = number


        type = input("Is this a mobile, home, or work phone? ")
        if type == "mobile":
            phone_number.type = addressbook_pb2.Person.MOBILE
        elif type == "home":
            phone_number.type = addressbook_pb2.Person.HOME
        elif type == "work":
            phone_number.type = addressbook_pb2.Person.WORK
        else:
            print
            "Unknown phone type; leaving as default value."


# Main procedure:  Reads the entire address book from a file,
#   adds one person based on user input, then writes it back out to the same
#   file.
if len(sys.argv) != 2:
  print("Usage:", sys.argv[0], "ADDRESS_BOOK_FILE")
  sys.exit(-1)

address_book = addressbook_pb2.AddressBook()

# Read the existing address book.
try:
  f = open(sys.argv[1], "rb")
  address_book.ParseFromString(f.read())
  f.close()
except IOError:
  print(sys.argv[1] + ": Could not open file.  Creating a new one.")

# Add an address.
AskForAddress(address_book.people.add())

# Write the new address book back to disk.
f = open(sys.argv[1], "wb")
f.write(address_book.SerializeToString())
f.close()
