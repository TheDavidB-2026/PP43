def create_account(owner, balance=0, history=None):
    if history is None:
        history = []
    return {"owner": owner, "balance": balance, "history": history}

def deposit(account, amount):
    if amount <= 0:
        return (False, "თანხა დადებითი უნდა იყოს")

    account["balance"] += amount
    if account["balance"] == int(account["balance"]):
        account["balance"] = int(account["balance"])

    amt_str = str(int(amount)) if amount == int(amount) else str(amount)
    account["history"].append(f"+{amt_str}")

    return (True, f"შეტანილია {amt_str} ლარი")

def withdraw(account, amount, fee=0.5):
    if amount <= 0:
        return (False, "თანხა დადებითი უნდა იყოს")

    total_needed = amount + fee
    if total_needed > account["balance"]:
        total_str = str(int(total_needed)) if total_needed == int(total_needed) else str(total_needed)
        return (False, f"არასაკმარისი ბალანსი (საჭიროა {total_str})")

    account["balance"] -= total_needed
    if account["balance"] == int(account["balance"]):
        account["balance"] = int(account["balance"])

    amt_str = str(int(amount)) if amount == int(amount) else str(amount)
    fee_str = str(int(fee)) if fee == int(fee) else str(fee)
    total_str = str(int(total_needed)) if total_needed == int(total_needed) else str(total_needed)

    account["history"].append(f"-{total_str}")
    return (True, f"გატანილია {amt_str} ლარი (საკომისიო {fee_str})")

def statement(account, last=3):
    balance_val = account["balance"]
    if balance_val == int(balance_val):
        balance_val = int(balance_val)

    print(f"--- {account['owner']} | ბალანსი: {balance_val} ---")

    ops = account["history"][-last:] if last > 0 else []
    for op in ops:
        print(op)

nino = create_account("ნინო", balance=100)
luka = create_account("ლუკა")

print(deposit(nino, 50))
print(deposit(nino, -10))
print(withdraw(nino, 30))
print(withdraw(nino, 500))
print(withdraw(nino, 20, fee=0))
print(deposit(luka, 15))

statement(nino)
statement(nino, last=1)
statement(luka)