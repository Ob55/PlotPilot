from functions import (
    list_caretakers,
    list_tenants,
    add_caretaker,
    add_tenant,
    ejject_caretaker,
    ejject_tenant,
    exit_program
)

def main():
    while True:
        print("1. to see all caretaker")
        print("2. to see all tenants")
        print("3. to add new caretaker")
        print("4. to add new tenant")
        print("5. to remove caretaker")
        print("6. to remove tenant")
        print("7. to exit program")

        userschoice = input("what do you want ")
        if userschoice == "1":
            list_caretakers()
        elif userschoice == "2":
            list_tenants()
        elif userschoice == "3":
            add_caretaker()

            input("Press Enter")
        elif userschoice == "4":
            add_tenant()
            input("Press Enter")
        elif userschoice == "5":
            print("Did not take rent")
            ejject_caretaker()
            input("Press Enter")
        elif userschoice == "6":
            print("Did not pay rent")
            ejject_tenant()
            input("Press Enter")

        elif userschoice == "7":
            exit_program()
        else:
            print("Invalid Input")

if __name__ =='__main__':
    main()