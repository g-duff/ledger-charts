import json
import re

import matplotlib.pyplot as plt


def condition(x):
    return re.match(r"expenses(?::[\w\s]+)$", x["account"])


with open("./july-expenses.json") as openfile:
    balance = json.load(openfile)

accounts = [b for b in balance if condition(b)]

amounts = [a["balance"] for a in accounts]
account_names = [a["account"] for a in accounts]

print(account_names)

fig, ax = plt.subplots()
ax.pie(amounts, labels=account_names, autopct="%1.1f%%")
plt.show()
