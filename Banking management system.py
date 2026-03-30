accounts = {}
acc_list = []
names = set()
def create():
    a = input("Acc No: ")
    if a in accounts:
        print("Exists")
        return
    n = input("Name: ")
    b = float(input("Balance: "))
    accounts[a] = (n, b)
    acc_list.append(a)
    names.add(n)
def deposit():
    a = input("Acc No: ")
    if a in accounts:
        amt = float(input("Amount: "))
        n, b = accounts[a]
        if amt > 0:
            accounts[a] = (n, b + amt)
        else:
            print("Invalid")
    else:
        print("Not found")

def withdraw():
    a = input("Acc No: ")
    if a in accounts:
        amt = float(input("Amount: "))
        n, b = accounts[a]
        if 0 < amt <= b:
            accounts[a] = (n, b - amt)
        else:
            print("Invalid / Low balance")
    else:
        print("Not found")
def view():
    for a in acc_list:
        print(a, accounts[a])
def search():
    s = input("Search name: ").lower()
    for a, (n, b) in accounts.items():
        if s in n.lower():
            print(a, n, b)
def total(lst):
    return 0 if not lst else accounts[lst[0]][1] + total(lst[1:])
while True:
    print("\n1.Create 2.Deposit 3.Withdraw 4.View 5.Search 6.Total 7.Names 8.Exit")
    c = input("Choice: ")
    if c == "1": create()
    elif c == "2": deposit()
    elif c == "3": withdraw()
    elif c == "4": view()
    elif c == "5": search()
    elif c == "6": print("Total:", total(acc_list))
    elif c == "7": print(names)
    elif c == "8": break
    else: print("Invalid")
