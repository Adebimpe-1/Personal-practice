expenses = []

def load_expenses():
    try:
        with open('expenses.txt', 'r') as file:
            for line in file:
                item, amount = line.strip().split(',')
                expenses.append({'item': item, 'amount': float(amount)})
    except FileNotFoundError:
        pass

def save_expenses():
    with open('expenses.txt', 'w') as file:
        for exp in expenses:
            file.write(f"{exp['item']},{exp['amount']}\n")

def add_expense(item, amount):
    expenses.append({'item': item, 'amount': amount})

def total_expenses():
    return sum(exp['amount'] for exp in expenses)

def main():
    load_expenses()
    while True:
        choice = input("1.Add expense 2.View total 3.Exit: ")
        if choice == '1':
            item = input("Enter expense item: ")
            amount = float(input("Enter amount: "))
            add_expense(item, amount)
            save_expenses()
        elif choice == '2':
            print(f"Total expenses: ${total_expenses():.2f}")
        elif choice == '3':
            break
        else:
            print("Invalid choice")

main()
