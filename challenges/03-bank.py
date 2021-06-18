print("Welcome to Chase bank.")
print("Have a nice day!")

# print("Welcome to Chase bank.")

# #current_balance = int(4000)

# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def bank_script(current_balance=4000):
#     print('Your current balance is', current_balance)
#     print('What would you like to do? (deposit, withdraw, check_balance')
#     choice = input('Enter choice: ')

#     if choice in ('deposit', 'withdraw', 'check_balance'):
    
#         if choice == 'deposit':
#             amount = int(input('How much would you like to deposit?\n'))
#             print('Your current balance is', add(current_balance, amount))
#             current_balance = add(current_balance, amount)
        
#         elif choice == 'withdraw':
#             amount = int(input('How much would you like to withdraw?\n'))
#             print('Your current balance is', subtract(current_balance, amount))
#             current_balance = subtract(current_balance, amount)
        
#         elif choice == 'check_balance':
#             print('Your current balance is', current_balance)
#     else:
#         print('Invalid input')
    
#     all_done = input('Are you finished? (Y/N)\n')

#     if all_done in ('Y', 'N'):
    
#         if all_done == 'Y':
#             print("Have a nice day!")
        
#         if all_done == 'N':
#             bank_script(current_balance)
            
# bank_script()

def bank():
    choice = input("What would you like to do? (deposit, withdraw, check_balance)?\n")
    if choice == "deposit":
        deposit()
    elif choice == "withdraw":
        withdraw()
    else:
        balance()

def balance():
    print(balance)
    done = input("Are you done?\n")
    if done == "yes": 
        print("Have a nice day!")
    else:
        bank()
   

def withdraw():
    choice = input("How much would you like to withdraw?\n")
    choice = int(choice)
    print(f"Current balance is now {total - choice}")
    done = input("Are you done?\n")
    if done == "yes": 
        print("Have a nice day!")
    else:
        bank()
    
    

def deposit():
    choice = input("How much would you like to deposit?\n")
    choice = int(choice)
    print(f"Current balance is now {total + choice}")
    done = input("Are you done?\n")
    if done == "yes": 
        print("Have a nice day!")
    else:
        bank()

bank()
