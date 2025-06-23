from abc import ABC, abstractmethod
from datetime import date, timedelta

# ------- Abstract parent class -------
class Librarysystem(ABC):
     def __init__(self, title, item_id):
          self.title =title
          self.item_id = item_id
          self.__status = "in"

     @property
     def status(self):
          return self.__status
     
     def _set_status(self, new):
          self.__status = new

     @abstractmethod
     #borrow rule
     def borrow(self):
        pass

     #return rule
     def return_item(self):
        if self.status == "in":
            print(f"{self.title} IN!")
            return False
        self._set_status("in")
        print(f"{self.title} Return!")
        return True

# ------- Subclasses -------    
#book 
class Book(Librarysystem):
    HOLD_DAYS = 30
    def borrow(self):
        if self.status == "out":
            print(f"{self.title} OUT")
            return False
        self._set_status("out")
        due = date.today() + timedelta(days=Book.HOLD_DAYS)
        print(f"success borrow,due: {due}")
        return True

#magazine   
class Magazine(Librarysystem):
     HOLD_DAYS = 14
     def borrow(self):
        if self.status == "out":
            print(f"{self.title} OUT")
            return False
        self._set_status("out")
        due = date.today() + timedelta(days=Magazine.HOLD_DAYS)
        print(f"success borrow,due: {due}")
        return True

#CD    
class CD(Librarysystem):
    HOLD_DAYS = 7
    def borrow(self):
        if self.status == "out":
            print(f"{self.title} OUT")
            return False
        self._set_status("out")
        due = date.today() + timedelta(days=CD.HOLD_DAYS)
        print(f"success borrow,due: {due}")
        return True


# ========= Member =========
class member:
     def __init__(everyMember, name, member_id):
          everyMember.name = name
          everyMember.member_id = member_id
          everyMember._borrowed = []

# memberBorrow
     def member_borrow(everyMember, item: Librarysystem):
         success_borrow =item.borrow()
         if success_borrow:
             everyMember._borrowed.append(item)
             print(f"{everyMember.name} sucess_borrow")
         else:
             print(f"{everyMember.name} fail")
     
 # memberReturn
     def member_Return(everyMember, item: Librarysystem):
         if item not in everyMember._borrowed:
             print(f"{everyMember.name} not borrow {item.title}")
             return
         success_return_item = item.return_item()
         if success_return_item:
             everyMember._borrowed.remove(item)
             print("success return")
         else:
             print("fail return")