"""
CLI
---------------
Enter command:
  items
  members
  borrow <member_id> <item_id>
  return <member_id> <item_id>
  quit

"""

from data import items, members

#Start the interaction
def main():
    print("library system, enter [help] search command")
    
    #first line of input
    while True:
        command = input("Enter command: ").strip().split()
        if not command: continue
        if command[0] == "help":
            print(__doc__)

        #List items
        elif command[0] == "items":
            for everything in items.values():
                print(f"{everything.title}   {everything.item_id}   {everything.status}")

        #List members
        elif command[0] == "members":
            for everybody in members.values():
                print(f"{everybody.name}   {everybody.member_id}")

        #borrow
        elif  command[0] == "borrow" and len(command) == 3:
            middle, last = command[1], command[2]
            if middle in members and last in items:
                members[middle].member_borrow(items[last])
            else:
                print("Member ID or Item ID does not exist")

        #return
        elif command[0] == "return" and len(command) == 3:
            middle, last = command[1], command[2]
            if middle in members and last in items:
                members[middle].member_Return(items[last])
            else:
                print("Member ID or Item ID does not exist")         

        #quit
        elif command[0] == "quit":
            break
        else:
            print("Invalid input, enter [help]")

if __name__ == "__main__":
    main()
