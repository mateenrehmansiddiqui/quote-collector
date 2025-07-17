from core import add_quote, list_quotes, delete_quote

def menu():


    while True:

        print("\n----QUOTE-COLLECTOR----\n")
        print("1. Add Quote")
        print("2. List Quotes")
        print("3. Delete Quote")
        print("4. Exit")
        choice = int(input("Choice: "))

        if choice == 1:
            quote = input("\nEnter Quote to add: \n")
            add_quote(quote)
        elif choice == 2:
            list_quotes()
        elif choice == 3:
            index = int(input("\nEnter index to delete quote from: \n"))
            delete_quote(index)
        elif choice == 4:
            exit()
        else:
            print("[!] Invalid Choice.")

menu()