class Book:
    def __init__(anybook, title, item_id):
        anybook.title = title
        anybook.item_id = item_id
        anybook.status = "in"

#borrow
def borrow(anybook):
        if anybook.status == "out":
            print(f"《{anybook.title}》OUT！")
            return False
        anybook.status = "out"
        return True 

#return
def return_item(anybook):
        if anybook.status == "in":
            print(f"《{anybook.title}》IN!")
            return False
        anybook.status = "in"
        return True

class Member:
     def __init__(everyMember, name, member_id):
          everyMember.name = name
          everyMember.member_id = member_id
          everyMember._borrowed = []

# memberBorrow
def member_borrow(everyMember,anybook:Book):
     success = anybook.borrow(anybook)
     if success:
        everyMember._borrowed.append(anybook)
        print(f"{everyMember.name} Borrow《{anybook.title}》")
     else:
        print(f"{everyMember.name} fail")

 # memberReturn