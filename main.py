from file_operations import FileOperations
from chat_operations import ChatOperations


# Displays Main menu choices
def general_queries():
    print("""
Welcome to the CLI Chatter!
Enter the options listed to look at a specific query: 
1) Start New Chat
2) Continue with an Existing Chat
3) Delete A Chat
Q) Quit
    """)
    
def main():
    general_queries()
    choice = input("> ").lower()
    while True:
        if choice == "1":
            chat = ChatOperations()
            chat.start_chart()
            break
        elif choice == "2":
            print("2")
            break
        elif choice == "3":
            print("3")
            break
        elif choice == "q":
            print("Program exited")
            quit()
        else:
            print("You entered a wrong choice. Please input choices between (1-3)")
            
            
if __name__ == "__main__":
    main()