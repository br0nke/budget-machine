import pickle
import os

BUDGET_FILE = 'budget_file.pickle'

def load_file():
    if os.path.exists(BUDGET_FILE):
        with open(BUDGET_FILE, "rb") as budget_file:
            budget_main = pickle.load(budget_file)
        return budget_main
    else:
        return {}

def save_file(budget_main):
    with open(BUDGET_FILE, "wb") as budget_file:
        pickle.dump(budget_main, budget_file)

def income(money_in, amount, budget_main):
    budget_main[money_in] = +abs(float(amount))
    print(f'Eur {amount} amount was added.')
    return budget_main

def expense(money_out, amount, budget_main):
    budget_main[money_out] = -abs(float(amount))
    print(f'Eur {amount} amount was deducted.')
    return budget_main

def statment(budget_main):
    for key, value in budget_main.items():
        print(f'{key}  {value}')
    return budget_main

def balance(budget_main):
    whole_budget = sum(budget_main.values())
    print(f'Current balance in Eur: {whole_budget:.2f}')
    return budget_main

budget_main = load_file()

while True:
    print(">>>> Budget Holes Checker <<<<")
    print("0: Exit")
    print("1: Add Income")
    print("2: Add Expense")
    print("3: Print Transactions List")
    print("4: Current Balance")
    choice = input("Choose your task: ")
    if choice == "0":
        save_file(budget_main)
        print('Bye bye :)')
        break
    elif choice == "1":
        money_in = input("Enter transaction name: ")
        amount = input('Enter the amount to add: ')
        budget_main = income(money_in, amount, budget_main)
    elif choice == "2":
        money_out = input("Enter deduction transaction name: ")
        amount = input("Enter deduction amount: ")
        budget_main = expense(money_out, amount, budget_main)
    elif choice == "3":
        statment(budget_main)
    elif choice == "4":
        balance(budget_main)
    else:
        print("Bad input check your numbers!")
        pass