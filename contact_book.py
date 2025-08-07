import os

def store_number(contact_entry):
    try:
        with open('contact_book.txt', 'a')as f:
            f.write(contact_entry.strip() + '\n')
            print("✅ Contact saved!\n")
    except Exception as e:
        print("\n⚠️  An unknown error occurred!")

def name_exists(name):
    try:
        with open("contact_book.txt", 'r')as f:
            lines = f.readlines()
            for line in lines:
                if line.lower().startswith(name.lower()):
                    return True
        return False
    except FileNotFoundError:
        return False

def add_contact_flow():
    while True:
        while True:
            name = input("\n✏️  Enter name: ").strip()
            if name_exists(name):
                print("❌ This name already exists.")
                try_again = input("👉 Try a different name?(Y/N): ").strip().upper()
                if try_again != "Y":
                    return
                continue
               
            else:
                
                break
                
        num= input("📞 Enter number: ").strip()

        contact_entry = (f"Name: {name}  | Ph: {num}\n")
        store_number(contact_entry)

        repeat = input("➕ Save more contact?: (Y/N): ").strip().upper()
        if repeat != 'Y':
            return


def view_contact():
    try:
        with open('contact_book.txt', 'r')as f:
            read = f.read()
            print('\n'+read)
            if not read.strip():
                print("⚠️  The contact book is empty.")
            
    except:
        print("⚠️  No contact book file found.")

def delete_contact(name_to_delete):
    try:
        with open('contact_book.txt', 'r')as f:
           lines = f.readlines()

        found = False

        with open('contact_book.txt', 'w')as f:
            for line in lines:
                contact_name = line.strip().split("Name:")[1].split("|")[0].strip()
                if contact_name.lower() != name_to_delete.lower():
                    f.write(line)
                else:
                    found= True
                
        if found:
            print("🚮 Delete sucessfully.")
        else:
            print("❌ Name not found in contact list.")
    except:
        print("⚠️  Eroor while deleting")


def search_contact(name):
    found = False
    try:
        with open('contact_book.txt', 'r')as f:
            contact = f.readlines()

            for contacts in contact:
                if name.lower() in contacts.lower():
                    print(f"Found:",contacts.strip())
                    found = True
        if not found:
            print("⚠️  Contact not found.")
    except FileNotFoundError:
        print("⚠️  Contact book is empty or missing")

def edit_name(old_name, new_name):
    try:
        with open('contact_book.txt', 'r')as f:
            lines = f.readlines()

        updated = False
        with open('contact_book.txt', 'w')as f:
            for line in lines:
                if old_name.lower() in line.lower():
                    line = line.replace(old_name, new_name)
                    updated = True
                f.write(line)
        if updated:
            print("✅ Name updated successfully")
        else:
            print("⚠️  Name not found")
    except FileNotFoundError:
        print("⚠️  Contact book is not found")

def main():
    while True:
        print("\n==== ☎️  Contact Book Menu ====")
        print("Press 1 to store number with name")
        print("Press 2 to view the contact list")
        print("Press 3 to delete contacts")
        print("Press 4 to search a contact")
        print("Press 5 to edit a contact")
        print("Press 6 to exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            add_contact_flow()
        

        elif choice == '2':
            view_contact()
            
            
        elif choice == '3':
            name_to_delete = input("\nEnter name to delete: ")
            delete_contact(name_to_delete)
            
        elif choice == '4':
            name = input("Search: ")
            search_contact(name)
        
        elif choice == '5':
            old_name = input("Enter contact name to edit: ")
            new_name = input("🔁 Enter new name: ")
            edit_name(old_name,new_name)
        
        elif choice == '6':
            print("👋 Goodbye")
            
            break

        else:
            print(" Invalid choice. Try again")


if __name__ == "__main__":
    main()