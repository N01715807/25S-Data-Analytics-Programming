### Library Borrowing System – Project Description

# Statement of Explanation

I am a part-time online student. Due to being unable to contact any group members before June 22, and because I had to travel to another city for work after that date, I was not able to participate in group collaboration during the June 22–25 window. Therefore, I independently completed all parts of this assignment, including development and documentation. I appreciate your understanding—thank you.

***

## Project Overview

This is a mini library management system developed using Object-Oriented Programming (OOP) principles. It demonstrates key OOP concepts such as:

- **Class inheritance**
- **Encapsulation**
- **Abstract methods**
- **Polymorphism**

The system allows users to perform basic transactions like borrowing and returning items through a simple **Command Line Interface (CLI)**.

### Key Features
- Support for managing **Books**, **Magazines**, and **CDs**
- Borrow and return logic based on item type
- Member management and transaction history
- Text-based CLI for user interaction

***

## File Structure
├── classes.py   # All class definitions (Librarysystem, Book, CD, member, etc.)  
├── data.py      # Data (books, members)  
├── main.py      # Main program with command-line interface logic  
└── README.md    # This documentation file 

## Command Usage:

Run the main program **python main.py**
After running the program, enter one of the following commands to operate:

- `help` – View help information  
- `items` – List all library items  
- `members` – List all registered members  
- `borrow <member_id> <item_id>` – Borrow a book, magazine, or CD  
- `return <member_id> <item_id>` – Return a borrowed item  
- `quit` – Exit the system  

Example:
***
borrow 200622615 10000002
return 200622615 10000002